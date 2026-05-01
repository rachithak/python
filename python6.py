marks=[]
for i in range (6):
    m=int(input("enter marks:"))
    marks.append(m)
    n=len(marks)
for i in range (n):
    for j in range(0,n-i-1):
        if marks[j]<marks[j+1]:
            temp=marks[j]
            marks[j]=marks[j+1]
            marks[j+1]=temp
print("marks from highest to lowest:")
for m in marks:
    print(m)