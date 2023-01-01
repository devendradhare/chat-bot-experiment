import pyttsx3

engine = pyttsx3.init()
engine.setProperty('voice', 'english')
engine.setProperty('rate', 150)


def speek(text):
    engine.say(text)
    engine.runAndWait()

#  this will print how many voices i have installed
# voices = engine.getProperty('voices')
# for voice in voices:
#     print(f"Name: {voice.name}")
#     print(f"Languages: {voice.languages}")
#     print(f"ID: {voice.id}")
#     print("---")
