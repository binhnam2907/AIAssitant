import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib 
import webbrowser as wb
import os 
import pyautogui
import psutil
import pyjokes 

from wikipedia.wikipedia import search

engine = pyttsx3.init()
'''
# edit voice and speed
voices = engine.getProperty('voices')
engine.setProperty('voices' , voices[0].id)
newVoiceRate = 150
engine.setProperty('rate', newVoiceRate)
'''
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The now day is")
    speak(date)
    speak(month)
    speak(year)
    
def wishme():
    speak("Welcome back Nam!")
    hour = datetime.datetime.now().hour

    if hour >= 6 and  hour <= 12 : 
        speak("Good moring ")
    elif hour > 12 and hour <= 18:
        speak("Good afternoon")
    elif hour > 18 and hour <= 24 : 
        speak("Good evening")
    else :
        speak("Good night")

    speak("How can i help you ?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ("Listening . . . ")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing . . . ")
        query = r.recognize_google(audio, 'en=US')
        print(query)
    except Exception as e:
        print(e)
        speak("Please say again please .... ")
    
        return "None"
    return query

def sendMail(to, content):
    sever = smtplib.SMTP('stmp.gamil.com', 587)
    sever.ehlo()
    sever.starttls()
    speak("Tell me your email")
    yourMail = takeCommand()
    speak("Tel me your password too ")
    yourPass = takeCommand()
    sever.login(yourMail, yourPass) #mat khau gmail 
    sever.sendmail("lnbinhnamhcmus@gmail.com", to , content)
    sever.close()

def screenShot():
    img = pyautogui.screenshot()
    img.save("Desktop\ss.png")

def cpu():
    usage = str(psutil.cpu_percent)
    speak("CPU is at " + usage)

    battery = psutil.sensors_battery
    speak("Battery is at ")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())

if __name__ == "__main__":

    wishme()

    while True:
        query = takeCommand().lower()
        print(query)
        
        if "time" in query:
            time()

        elif "date" in query:
            date()

        elif "exit" in query:
            quit()
            
        elif "wikipedia" in query:
            speak("Searching . . . ")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentence = 2)
            speak(result)

        elif "send email" in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                speak("Who is take this email?")
                to = takeCommand()
                #to = "xyz@gmail.com" #email nhan
                sendMail(to, content)
                speak("Email sent succesfully ")
            except Exception as e:
                speak(e)
                speak("Unable to send the email")

        elif "search in chrome" in query:
            speak("What should i search?")
            chromepath = "C:\Program Files\Google\Chrome\Application\chrome.exe %s"
            #ban co the thay doi duong dan cua ban
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")

        elif "logout" in query:
            os.system("shutdown - 1")

        elif "shutdown" in query:
            os.system("shutdown /s /t 1")

        elif "restart" in query:
            os.system("shutdown /r /t 1")

        elif "remember that" in query:
            speak("What should i remember ?")
            data = takeCommand()
            speak("You said me to remember" + data + "really")
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()

        elif "do you know anything" in query:
            remember = open("data.txt", "r")
            speak("you said me to remeber that" + remember.read())

        elif "screenshot" in query:
            screenShot()
            speak("Already done")
        
        elif "cpu" in query:
            cpu()

        elif "joke" in query:
            jokes()


