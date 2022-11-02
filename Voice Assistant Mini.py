import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pyjokes
import pywhatkit

listener=sr.Recognizer()
engine=pyttsx3.init()

#voices=engine.getProperty('voices')
#engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_command():
    try:
        with sr.Microphone() as source:
            print("Mini...working")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            
            if 'mini' in command:
                command=command.replace("mini","")
                print(command)
            elif 'hey mini' in command:
                talk('Your mini here')
                talk('how can i help you')
    except:
        print("Ooops! mike is not working")

    return command

def run_mini():
    command=get_command()

    if "play" in command:
        song = command.replace("play","")
        pywhatkit.playonyt(song) 

    if 'time' in command:
        time=datetime.datetime.now().strftime('%I %M %p')
        print(time)
        talk("Now time is"+time)

    elif 'date' in command:
        date=datetime.date.today().strftime('%B %d %Y')
        print(date)
        talk("Today is"+date)
    elif 'tell me about' in command:
        things=command.replace('tell me about','')
        info=wikipedia.summary(things,2)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk("i cannot understand")
        talk("can you tell me once again")

while 1:
    run_mini()