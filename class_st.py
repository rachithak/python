class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"name:{self.name}, age:{self.age}"
s=student("ravi",20)
print(s)