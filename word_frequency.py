text=input("enter a paragraph:\n")
words=text.lower().split()
frequency={}
for word in words:
    word=word.strip(".,!;:?")
    if word in frequency:
        frequency[word]+=1
    else:
        frequency[word]=1
print("\nWord Frequencies:")
for word,count in frequency.items():
    print(word,":",count)