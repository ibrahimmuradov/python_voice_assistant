# -*- coding: utf-8 -*-

import speech_recognition as sr
from datetime import datetime
from playsound import playsound
from gtts import gTTS
import random
import os

r = sr.Recognizer()
mic = sr.Microphone()

# listen mic
def mic_text_doc():
    text = ''
    with mic as m:
        print('Listening..')
        r.pause_threshold = 1
        audio = r.listen(m, phrase_time_limit=5)

        try:
            text = r.recognize_google(audio, language='en-EN')
        except sr.UnknownValueError:
            print(" -- I don't understand you -- ")
    return text

# change text data to speak
def text_to_speak(data):
    tts = gTTS(data, lang="en")
    rand = random.randint(1, 1000000)
    file = "audio-"+str(rand)+".mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)


flag = True
# search world
while flag:
    text = mic_text_doc().lower()
    print("You: ", text)

    worlds = {
        "exit": "OK, exiting program",
        "hi": "Hello Sir",
        "hello": "hi sir",
        "can you hear me": "Yes, I can hear you",
        "how are you": "I am fine and you",
        "oru": "I am fine and you",
        "i am also good": "Great",
        "thank you": "Welcome",
        "what are you doing": "I'm learning new things",
        "what time is it": datetime.now().strftime("%H:%M")
    }

    if text in worlds.keys():
        answer = worlds[text]
        text_to_speak(answer)

        if text == "exit":
            flag = False
            break