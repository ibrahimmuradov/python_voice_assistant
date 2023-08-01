# -*- coding: utf-8 -*-

import speech_recognition as sr
from playsound import playsound
from gtts import gTTS
from words import words
import random
import os

rcognizer = sr.Recognizer()
microphone_sound = sr.Microphone()

# listen mic
def mic_text_doc():
    sound_text = ''
    with microphone_sound as microphone:
        print('Listening..')
        rcognizer.pause_threshold = 1
        audio = rcognizer.listen(microphone, phrase_time_limit=5)

        try:
            sound_text = rcognizer.recognize_google(audio, language='en-EN')
        except sr.UnknownValueError:
            print(" -- I don't understand you -- ")
    return sound_text

# change text data to speak
def text_to_speak(data):
    sound_file = gTTS(data, lang="en")
    generate_random_number = random.randint(1, 1000000)
    file_name = "audio-"+str(generate_random_number)+".mp3"
    sound_file.save(file_name)
    playsound(file_name)
    os.remove(file_name)

flag = True
# search word
while flag:
    text = mic_text_doc().lower()
    print("You: ", text)

    if text in words.keys():
        answer = words[text]
        text_to_speak(answer)

        if text == "exit":
            flag = False
            break
