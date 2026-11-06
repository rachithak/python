from flask import (
    Flask, render_template, request, redirect,
    url_for, flash
)
import sqlite3
from pathlib import Path
from datetime import date, timedelta

app = Flask(__name__)

# Used for session-based flash messages.
# Replace this development key before deployment.
app.secret_key = "change-this-development-key"

# Store the database beside app.py.
BASE_DIR = Path(__file__).resolve().parent
DATABASE = BASE_DIR / "database.db"


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def initialize_database():
    with get_db_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS food_items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                quantity REAL NOT NULL,
                unit TEXT NOT NULL,
                purchase_date TEXT NOT NULL,
                expiry_date TEXT NOT NULL
            )
        """)

        conn.execute("""
            CREATE TABLE IF NOT EXISTS used_food (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                food_name TEXT NOT NULL,
                quantity REAL NOT NULL,
                unit TEXT NOT NULL,
                used_date TEXT NOT NULL
            )
        """)

def get_status(expiry_date):
    expiry = date.fromisoformat(expiry_date)
    days_left = (expiry - date.today()).days

    if days_left < 0:
        return "Past expiry date", "expired"
    elif days_left == 0:
        return "Expires today", "urgent"
    elif days_left <= 3:
        return f"Expires in {days_left} day(s)", "urgent"
    elif days_left <= 7:
        return f"Expires in {days_left} days", "soon"
    else:
        return "Fresh", "fresh"


@app.route("/")
def home():
    return render_template("index.html")
@app.route("/dashboard")
def dashboard():
    today = date.today()
    three_days_later = today + timedelta(days=3)

    with get_db_connection() as conn:
        total_items = conn.execute(
            "SELECT COUNT(*) FROM food_items"
        ).fetchone()[0]

        expiring_soon = conn.execute("""
            SELECT COUNT(*) FROM food_items
            WHERE expiry_date >= ? AND expiry_date <= ?
        """, (
            today.isoformat(),
            three_days_later.isoformat()
        )).fetchone()[0]

        expired_items = conn.execute("""
            SELECT COUNT(*) FROM food_items
            WHERE expiry_date < ?
        """, (today.isoformat(),)).fetchone()[0]

        # Retrieve all items that need an expiry warning.
        rows = conn.execute("""
            SELECT id, name, quantity, unit, expiry_date
            FROM food_items
            WHERE expiry_date <= ?
            ORDER BY expiry_date ASC
        """, (three_days_later.isoformat(),)).fetchall()

    notifications = []

    for row in rows:
        item = dict(row)
        item["status"], item["status_class"] = get_status(
            item["expiry_date"]
        )
        notifications.append(item)

    return render_template(
        "dashboard.html",
        total_items=total_items,
        expiring_soon=expiring_soon,
        expired_items=expired_items,
        notifications=notifications
    )


@app.route("/inventory", methods=["GET", "POST"])
def inventory():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        unit = request.form.get("unit", "")
        purchase_text = request.form.get("purchase_date", "")
        expiry_text = request.form.get("expiry_date", "")

        allowed_units = {
            "pieces", "kg", "g", "litres", "ml", "packs"
        }

        try:
            quantity = float(request.form.get("quantity", ""))
            purchase_date = date.fromisoformat(purchase_text)
            expiry_date = date.fromisoformat(expiry_text)

            if not name or len(name) > 100:
                raise ValueError("Enter a food name of up to 100 characters.")

            if not 0 < quantity <= 100000:
                raise ValueError("Quantity must be greater than zero.")

            if unit not in allowed_units:
                raise ValueError("Select a valid unit.")

            if purchase_date > date.today():
                raise ValueError("Purchase date cannot be in the future.")

            if expiry_date < purchase_date:
                raise ValueError(
                    "Expiry date cannot be before purchase date."
                )

        except (ValueError, TypeError):
            flash(
                "Check the food details, quantity and dates, then try again.",
                "error"
            )
            return redirect(url_for("inventory"))

        with get_db_connection() as conn:
            conn.execute("""
                INSERT INTO food_items
                    (name, quantity, unit, purchase_date, expiry_date)
                VALUES (?, ?, ?, ?, ?)
            """, (
                name, quantity, unit,
                purchase_text, expiry_text
            ))

        flash(f"{name} was added to your inventory!", "success")
        return redirect(url_for("inventory"))

    with get_db_connection() as conn:
        rows = conn.execute("""
            SELECT * FROM food_items
            ORDER BY expiry_date ASC, id DESC
        """).fetchall()

    items = []
    for row in rows:
        item = dict(row)
        item["status"], item["status_class"] = get_status(
            item["expiry_date"]
        )
        items.append(item)

    return render_template("inventory.html", items=items)


@app.route("/delete/<int:item_id>", methods=["POST"])
def delete_item(item_id):
    with get_db_connection() as conn:
        cursor = conn.execute(
            "DELETE FROM food_items WHERE id = ?",
            (item_id,)
        )

    if cursor.rowcount:
        flash("Food item deleted.", "success")
    else:
        flash("Food item was not found.", "error")

    return redirect(url_for("inventory"))


initialize_database()
@app.route("/mark_used/<int:item_id>", methods=["POST"])
def mark_used(item_id):
    with get_db_connection() as conn:
        item = conn.execute(
            "SELECT * FROM food_items WHERE id = ?",
            (item_id,)
        ).fetchone()

        if item is None:
            return redirect(url_for("inventory"))

        # Save the food in history FIRST.
        conn.execute("""
            INSERT INTO used_food
                (food_name, quantity, unit, used_date)
            VALUES (?, ?, ?, ?)
        """, (
            item["name"],
            item["quantity"],
            item["unit"],
            date.today().isoformat()
        ))

        print("USED FOOD COUNT:",
              conn.execute(
                  "SELECT COUNT(*) FROM used_food"
              ).fetchone()[0])
    # Delete from inventory only after saving succeeds.
        conn.execute(
            "DELETE FROM food_items WHERE id = ?",
            (item_id,)
        )

    return redirect(url_for("inventory"))
@app.route("/used-food")
def used_food_history():
    with get_db_connection() as conn:
        used_items = conn.execute("""
            SELECT food_name, quantity, unit, used_date
            FROM used_food
            ORDER BY used_date DESC, id DESC
        """).fetchall()

    return render_template(
        "used_food.html",
        used_items=used_items
    )

    if __name__ == "__main__":  
        app.run(debug=True)