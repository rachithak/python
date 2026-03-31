def prime(num):
    if num<=1:
        return"not prime"
    for i in range(2,num):
        if num%i==0:
            return"not prime"
    return "prime"
number=int(input("enter number:"))
result=prime(number)
print("the number is=",result)
