def factorial_module(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
import factorial_module

n = 5
r = 2

result = factorial_module.factorial(n) // (
    factorial_module.factorial(r) *
    factorial_module.factorial(n-r)
)

print("Binomial Coefficient =", result)