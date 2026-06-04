def reverse_string(self):
    if len(self)==0:
        return self
    return reverse_string(self[1:])+self[0]
text="python"
print(reverse_string(text))