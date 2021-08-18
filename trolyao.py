import pyttsx3
import datetime
import speech_recognition as sr

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


    
   
