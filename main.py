
import os
import pyttsx3

if __name__ == '__main__':
    print("Welcome! स्वागत है!")
    engine = pyttsx3.init()
    engine.setProperty('rate', 4)
    while True:
        language = input("Enter '1' for English or '2' for Hindi (1/2): ")
        if language == '1':
            engine.setProperty('voice', 'en')
            break
        elif language == '2':
            engine.setProperty('voice', 'hi')
            break
        else:
            print("Invalid input. Please enter '1' for English or '2' for Hindi.")

    while True:
        x = input("What do you want me to pronounce: ")
        if x.lower() == "q":
            break
        engine.say(x)
        engine.runAndWait()
