import string
def remove_punctuation(my_story):
    phrase_sans_punct=""
    for letter in my_story:
        if letter not in string.punctuation:
            phrase_sans_punct+=letter
    return phrase_sans_punct
my_story="""
the way of the program:the python programming language,what is a program?what is debugging?
syntax errors,runtime error,sematic errors,experimental debugging.
variables,etc.
"""
words=remove_punctuation(my_story).split()
print(words)