num=int(input("enter numbers"))
sum=0
while num>0:
    digit=num%10
    sum=sum+digit
    num=num//10
print("sum of number is",sum)