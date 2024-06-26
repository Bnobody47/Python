import pyttsx3

data = input("Enter text whic you can turn in to speech:\n")

engine = pyttsx3.init()
engine.say(data)
engine.runAndWait()