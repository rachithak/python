letter_counts={}
for letter in "mississippi":
    letter_counts[letter]=letter_counts.get(letter,0)+1
print(letter_counts)
