student={}
n=int(input("enter number of student:"))
for i in range(n):
    name=input("enter student name:")
    marks=float(input("enter marks:"))
    student[name]=marks
print("\n student records:")
for name,marks in student.items():
    print(name,":",marks)
avg=sum(student.values())/len(student)
print("\n average marks:",avg)
topper=max(student,key=student.get)
print("topper:",topper,"with",student[topper],"marks")
