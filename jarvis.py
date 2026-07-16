#welcome
speak("hello Rachitha, i am jarvis.")
while True:
    command=take_command()
    if command == "":
        continue
    #greeting
    if "hello" in command:
        speak("hello Rachitha")
    