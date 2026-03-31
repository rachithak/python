def check_even_or_odd(num):
    if num%2==0:
        return("even")
    else:
        return("odd")
number=int(input("enter a number:"))
#calling the function
result=check_even_or_odd(number)
print("the number is:",result)