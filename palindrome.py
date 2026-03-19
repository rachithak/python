num=int(input("enter number:"))
rev=0
original=num
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
if original==rev:
    print(rev," is palindrome")
else:
    print(rev,"is not a palindrome")