
'''
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       -  api key
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        - new key

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       - svgsvg781 using now
'''

import keyboard
import pygetwindow as gw
import pyautogui
import time
import openai
import pyttsx3  #converts text to speech
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser  #to open the commanded application in browser
import os.path  #required to fetch the contents from the specified folder/directory
import smtplib  #to work with queries regarding e-mail
from config import apikey
import os
from AppOpener import open
import subprocess

engine = pyttsx3.init(
    'sapi5')  #API for voice recognition
voices = engine.getProperty('voices')  #gets us the details of the current voices
engine.setProperty('voice', voices[1].id) #1-female voice


def ai(prompt):
    openai.api_key = apikey

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # todo: Wrap this inside of a  try catch block
    # print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(text)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()  #the assistant won't be audible to us

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning')

    elif hour > 12 and hour < 18:
        speak('Good Afternoon')

    else:
        speak('Good Evening')

    speak('Hello Sir')#, I am KRONOS, your A.I. assistant. Please tell me how may I help you')


def takecommand():  #function to take an audio input from the user
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 2
        audio = r.listen(source)

    try:  # error handling
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')

    except Exception as e:
        print('Say that again please...')  #'say that again' will be printed in case of improper voice
        return 'None'
    return query


def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('senders_eamil@gmail.com', 'senders_password')
    server.sendmail('senders_email@gmail.com', to, content)
    server.close()


if __name__ == '__main__':  # for main execution
    wishme()
    while True:
        query = takecommand().lower()  #converts user asked query into lower case

        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=5)
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'play music' in query:
            speak('okay sir')
            music_dir = 'music_dir_of_the_user'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[1]))


        elif 'time' in query:
            strtime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'Sir the time is {strtime}')


        elif 'chat' in query:
            webbrowser.open('https://chat.openai.com/')

        elif 'netflix' in query:
            webbrowser.open('netflix.com')

        elif 'gfg' in query:
            webbrowser.open('geeksforgeeks.org')

        elif 'email' in query:
            try:
                speak('what should i write in the email?')
                content = takecommand()
                to = 'svgsvg781@gmail.com'
                sendemail(to, content)
                speak('email has been sent')
            except Exception as e:
                print(e)
                speak('Sorry, I am not able to send this email')

        elif 'exit' in query:
            speak('okay sir, see you soon')     
            quit()

        elif 'open' in query:
            app = query.replace("open ", "")
            time.sleep(1)
            keyboard.press_and_release('cmd')
            time.sleep(0.5)
            keyboard.write(app)
            time.sleep(0.5)
            keyboard.press_and_release('enter')

        elif 'copy' in query:
            keyboard.press_and_release('ctrl + c')

        elif 'select all and copy' in query:
            keyboard.press_and_release('ctrl + a')
            time.sleep(0.1)
            keyboard.press_and_release('ctrl + c')

        # elif 'go to' in query:
        #     windows = gw.getAllTitles()
        #     windows = [item for item in windows if item]
        #     for i in range(len(windows)):
        #         windows[i] = windows[i].lower()
        #     window_title = query.replace("go to ", "")
        #     target_window = None
        #     for window in windows:
        #         if window_title in window:
        #             target_window = window
        #             break
        #     if target_window:
        #         # Activate (bring to foreground) the target window
        #         pyautogui.getWindowsWithTitle(target_window).activate()
        #     else:
        #         print(f"Window '{window_title}' not found.")
        #         print("open windows are : ", windows)

