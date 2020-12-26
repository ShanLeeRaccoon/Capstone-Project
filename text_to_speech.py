import pyttsx3


engine = pyttsx3.init()

engine.say("Hello")
engine.runAndWait()
engine.stop()

volume = engine.getProperty("volume")
print(volume)

rate = engine.getProperty("rate")
print(rate)