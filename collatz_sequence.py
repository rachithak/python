n=int(input("enter a number:"))
steps=0
print("collatz sequence:")
while n!=1:
    print(n,end=" ")
    if n%2==0:
        n=n//2
    else:
        n=3*n+1
    steps+=1
print(1)
print("steps taken:",steps)