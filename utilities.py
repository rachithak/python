def square(n):
    return n*n
def cube (n):
    return n*n*n
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
n=int(input("enter values of n:"))
print("square=",square(n))
print("cube=",cube(n))
print("factorial=",factorial(n))