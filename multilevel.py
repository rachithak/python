class Father:
    def show_father(self):
        print("Father Property")

class Mother:
    def show_mother(self):
        print("Mother Property")

class Child(Father, Mother):
    def show_child(self):
        print("Child Property")

c = Child()

c.show_father()
c.show_mother()
c.show_child()