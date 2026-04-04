def sum_natural(n):
    if n==1:
        return 1
    else:
        return n + sum_natural(n-1)
n=int(input("enter a number:"))
result=sum_natural(n)
print("sum of first",n,"natural numbers is:",result)