import math
n=int(input("enter number of element:"))
numbers=[]
for i in range (n):
    num=float(input("enter number:"))
    numbers.append(num)
mean=sum(numbers)/n
variance=sum((x-mean)**2 for x in numbers)/n
std_dev=math.sqrt(variance)
print("numbers:",numbers)
print("mean=",mean)
print("variance=",variance)
print("standerd deviation=",std_dev)