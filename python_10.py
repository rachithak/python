class complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
n=int(input("enter number of complex numbers(>=2:)"))
real_sum=0
imag_sum=0
for i in range(n):
    print("complex number",i+1)
    r=float(input("enter real part:"))
    im=float(input("enter imaginary part:"))
    c=complex(r,im)
    real_sum+=c.real
    imag_sum+=c.imag
print("sum of",n,"complex numbers=",real_sum,"+",imag_sum,"i")