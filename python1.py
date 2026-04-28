num1=float(input("enter first numbers:"))
num2=float(input("enter second numbers:"))
print("choose operation:")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")
choice=int(input("enter your choice(1/2/3/4):"))
if choice==1:
    print("result:",num1+num2)
elif choice==2:
    print("result:",num1-num2)
elif choice==3:
    print("result:",num1*num2)
elif choice==4:
    if num2!=0:
        print("result:",num1/num2)
    else:
        print("division by zero is not allowed")
else:
    print("invalid choice")