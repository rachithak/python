a=int(input("enter first numbers:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
if a>b and a>c:
    print(a,"is largest")
elif b>c and b>a:
    print(b,"is largest")
else:
    print(c,"is largest")