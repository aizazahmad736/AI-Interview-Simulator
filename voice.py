import pyttsx3

engine = pyttsx3.init()

# Adjust speaking speed
engine.setProperty("rate", 170)

# Adjust volume (0.0 to 1.0)
engine.setProperty("volume", 1.0)


def speak(text):
    engine.say(text)
    engine.runAndWait()