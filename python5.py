num=input("enter a multi-digit number:")
freq={}
for digit in num:
    if digit in freq:
        freq[digit]+=1
    else:
        freq[digit]=1
print("digit frequence:")
for digit in freq:
    print("digit",digit,"appears",freq[digit],"times")