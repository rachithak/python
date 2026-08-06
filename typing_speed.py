import time
sentence="python programming is fun ang easy to learn"
print("====== Typing speed test ======")
print("type the following sentence exactly:\n")
print("sentence")
input("\nPress Enter when you are ready...")
start=time.time()
typed=input("\nstart typing:\n")
end=time.time()
time_taken=end-start
word_count=len(sentence.split())
wpm=(word_count/time_taken)*60
print("\n--------Result--------")
print(f"Time Taken:{time_taken:.2f} words per minute(WPM)")
if typed==sentence:
    print("Accuracy:100%")
    print("excellent! you typed the sentence correctly.")
else:
    correct=0
    for i in range(min(len(sentence),len(typed))):
        if sentence[i]==typed[i]:
            correct+=1
    accuracy=(correct/len(sentence))*100
    print(f"accuracy:{accuracy:.2f}%")
    print("there were some tying mistakes.s")
