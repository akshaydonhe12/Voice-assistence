import pyttsx3
import datetime
import speech_recogncition as sr
import wikipedia
import webbrowser



engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[13].id)


def speak(text):
  print(f'[JARVIS]: {text}')
  engine.say(text)
  engine.runAndWait()