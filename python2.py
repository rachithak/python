name=input("enter your name:")
year=int(input("enter your year of birth:"))
current_year=2026
age=current_year-year
if age>=60:
    print(name,"is a senior citizen.")
else:
    print(name,"is not a senior citizen")