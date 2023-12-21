import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes



listener = sr.Recognizer()
alexa = pyttsx3.init()
voices = alexa.getProperty('voices')
alexa.setProperty('voice' , voices[1].id)


def talk(text):
    alexa.say(text)
    alexa.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()                    
            if 'alexa' in command:
                command = command.replace('alexa' , '')

    except:
        pass
    return command

def run_alexa():
    command = take_command()


    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk("Current Time Is " + time)

    elif 'play' in command:
        song = command.replace('play' , '')
        talk('Playing' + song)
        pywhatkit.playonyt(song)

    elif 'tell me about' in command:
        look_for = command.replace('tell me about' , '')
        info = wikipedia.summary(look_for , 1)
        print(info)
        talk(info)

    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)

    elif 'date' in command:
        talk('Sorry Brother,I am in a Relationsheep with Shamim')

    else:
        talk("I Didn't get it but I am Going to search it in Google For You")
        pywhatkit.search(command)
    


while True:
    run_alexa()