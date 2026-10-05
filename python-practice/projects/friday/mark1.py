# VirtuL assistant --> make conversation,locate maps,greetigs
# TTS-->gTTS(Google text to speech)-->pip install gTTs

import gtts
from gtts import gTTS
import playsound
import speech_recognition as sr
from time import ctime #it returns current time
import os
import uuid
import webbrowser
import random
import pyqrcode
import png


# now we will give a text and convert to audio
# text="Systems online, boss. Ready when you are."
# g=gTTS(text)
# save as audio file(.mp3)
# g.save('audio.mp3')
# playsound.playsound('audio.mp3')

# let us make our virtualAssistant to understand what we speak
# SpeechRecognition(STT)
def listen():
    'SpeechRecognition'
    # we will make our system to check the microphone as source
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('i am  listening boss')
        audio=r.listen(source,phrase_time_limit=5)
    # what ever we speak lets store in data
    data=""
    # now we will give our Exception handling here to avoid any errors
    try:
        data =r.recognize_google(audio,language='en-US')
        print('got it boss:',data)
    except sr.UnknownValueError:
        print("boss i can't hear you boss")
    except sr.RequestError:
        print('Request is failed boss, please check your internet boss')
    return data
    # text=gTTS(data)
    # text.save('new.mp3')
    # playsound.playsound('new.mp3')
# listen() #needs to have pyaudio-->pip install pyaudio

# we will create separate functions for responding back and virtual
# assistant actions

def respond(string):
    'responding functions to get audio saved and text is spoken back'
    print(string)
    tts=gTTS(text=string)
    # now we want only text to be modified in the audio file
    tts.save('speech.mp3')
    # we will use above audio file and modify the content in it
    filename='speech%s.mp3'%str(uuid.uuid4())
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)
# next we will make our virtualassistant to function

# rock paper scissors
def RPS():
    choices=['rock','paper','scissors']
    respond('choose rock,paper or scissors')
    user=listen().lower()
    computer=random.choice(choices)
    print('your choice boss:',user)
    print('computer:',computer)

    if user==computer:
        respond("It's a tie boss")
    elif (
        (user == "rock" and computer == "scissors")
        or
        (user == "paper" and computer == "rock")
        or
        (user == "scissors" and computer == "paper")
    ):
        respond("You won boss")

    else:
        respond("I won boss")

# create qr
def create_qr():
    respond("Tell me the link")

    link = listen()

    qr = pyqrcode.create(link)

    qr.png("myqr.png", scale=6)

    respond("QR code created boss")


 
def va(data):
    'now we will map our conditions'
    if 'hello' in data:
        listening=True
        respond('hey boss.Ready to assist you whenever you need.')
    elif 'how are you' in data:
        listening=True
        respond('i am good boss')
    elif 'time'in data:
        listening=True
        respond(f"The current time is {ctime()}")
    elif "open Google" in data:
        listening=True
        url="https://www.google.com"
        respond('opening google boss')
        webbrowser.open(url) 
    elif 'locate' in data:
        listening=True
        url='https://www.google.com/maps/search/'+data.split("locate")[-1]
        respond('opening boss')
        webbrowser.open(url)
    elif 'play song'in data:
        listening=True
        url="https://youtu.be/JqFzhcWo3EU?si=keJ0CHGNmDkis_ss"
        respond('done boss')
        webbrowser.open
    elif 'game' in data:
        listening=True
        RPS()
    elif "QR" in data:
        listening = True
        create_qr()
    
    elif 'stop' in data or 'exit' in data or 'bye' in data:
        listening=False
        respond('have a good day boss')
    try:
        return listening
    except UnboundLocalError:
        print("i can't hear you boss")
respond('hey boss.')
listening=True
while listening:
    data=listen()
    listening=va(data)


