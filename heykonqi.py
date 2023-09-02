import speech_recognition as sr
import pyttsx3
import random
from datetime import datetime
import json

engine = pyttsx3.init()
voices = engine.getProperty("voices")


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def checkKeywordsInCommand(commandstr: str, keywords: list[str]) -> bool:
    command = commandstr.split()
    if keywords[0] in command:
        for keyword in keywords:
            for word in command:
                if keyword == word.lower():
                    index = command.index(keyword)
                    command = command[index + 1 :]  # type: ignore
                    break
            else:
                return False
        return True
    else:
        return False


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Now listening")
        r.pause_threshold = 1
        audio = r.listen(source)

    print("Deciphering")
    query = r.recognize_vosk(audio, language="en")
    query = json.loads(query)["text"]
    print("You Said: " + query)

    return query


while True:
    command = takeCommand()
    # Conversational
    if "katie" in command or "eighty" in command:
        # It's about us!
        try:
            start = command.lower().split().index("katie")
        except ValueError:
            start = command.lower().split().index("eighty")
        command = " ".join(command.split()[start + 1 :]).lower()
        print(command)
        # Tasks
        if checkKeywordsInCommand(command, ["what" "time"]):
            now = datetime.now()
            current_time = now.strftime("%H:%M")
            speak("It's " + current_time)

        if "random number" in command:
            randInt = random.randint(0, 10)
            speak("A random number between 0 and 10 is " + str(randInt))
