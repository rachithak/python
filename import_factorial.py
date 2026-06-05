def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

n = 5
r = 2

result =factorial(n) // (
    factorial(r) *
    factorial(n-r)
)

print("Binomial Coefficient =", result)