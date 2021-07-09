import pyttsx3
import datetime
import speech_recognition as sr



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


if __name__ == "__main__":
    wishMe()
    takeCommand()