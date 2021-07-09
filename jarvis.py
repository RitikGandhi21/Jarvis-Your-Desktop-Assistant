import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib



engine=pyttsx3.init('espeak')
voices=engine.getProperty('voices')
# print(voices[14].id)
engine.setProperty('voice',voices[13].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good afternoon!")

    else:
        speak("Good evening!")

    speak("I am Jarvis sir! Please tell me how may I help you?")




def takeCommand():
    # takes microphone input from the user and returns stirng output

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing ...")
        query=r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)

        print("Say that again please....")
        return "None"
    return query


def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('rastyrock21@gmail.com','9893530206')
    server.sendmail('rastyrock21@gmail.com',to,content)
    server.close()



if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia....")
            query=query.replace("wikipedia", "")
            results=wikipedia.summary(query,sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open gfg' in query:
            webbrowser.open("geeksforgeeks.org")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,The time is {strTime}")

        elif 'close jarvis' in query:
            speak("Good bye sir and have a good day!")
            exit()

        elif 'email to pulkit' in query:
            try:
                speak("What should I say?")
                content=takeCommand()
                to="pulkit020609@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")

            except Exception as e:
                print(e)
                speak("Sorry my friend ritik bhai. I am not able to send this email")

