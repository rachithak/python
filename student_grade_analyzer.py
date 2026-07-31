num_students=int(input("enter the number of student:"))
students=[]
for i in range(num_students):
    print(f"\nstudent{i+1}")
    name=input("enter student name:")
    marks=float(input("enter marks(out of 100):"))
    if marks>=90:
        grade="A+"
    elif marks>=80:
        grade="A"
    elif marks>=70:
        grade="B"
    elif marks>=60:
        grade="C"
    elif marks>=50:
        grade="d"
    else:
        grade="F"
    students.append((name,marks,grade))
highest=max(students,key=lambda X:X[1])
lowest=min(students,key=lambda X:X[1])
average=sum(student[1] for student in students)/num_students
print("\n----- student report-----")
for student in students:
    print(f"name:{student[0]},marks:{student[1]},grade:{student[2]}")
print("\n----- analysis-----")
print(f"average marks:{average:.2f}")
print(f"highest scorer:{highest[0]}({highest[1]})")
print(f"lowest scorer:{lowest[0]}({lowest[1]})")

