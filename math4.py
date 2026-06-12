def DIV(a,b):
    assert a>0,f"asserton error:'a' must be greater than 0,but got a={a}"
    if b==0:
        raise valueerror("valuerror:'b' cannot be zero_division by zero is undefined")
        c=a/b
        return c
try:
    a=float(input("enter value of a:"))
    b=float(input("enter value of b:"))
    result=DIV(a,b)
    print(f"result c={a}/{b}={result}")
except assertionerror as ae:
    print(f"assertion failed->{ae}")
except valueerror as ve:
    print(f"value error caught->{ve}")
except exception as e:
    print(f"unexpected error->{e}")