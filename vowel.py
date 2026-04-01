sentence=input("enter a sentence:")
vowels="aeiou"
count=0
for ch in sentence.lower():
    if ch in vowels:
        count+=1
print("number of vowels in the sentence:",count)