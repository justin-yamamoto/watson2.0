import pyttsx3
import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)
engine.say('hello my name is watson')
engine.say('how may i help')
# v in voices:
 #print(v)

engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        print('listening...')
        with sr.Microphone() as source:
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'watson' in command:
                command = command.replace('watson', '')
                print(command)
    except:
        pass
    return command

def run_watson():
    command = take_command()
    print(command)

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        talk('it is ' + time)

    elif 'date' in command:
        date = datetime.date.today()
        talk(date)

    elif 'who' in command:
        person = command.replace('who', '')
        info = wikipedia.summary(person, 3)
        print(info)
        talk(info)
    elif 'how' in command:
        directions = command.replace('how', '')
        instructions = wikipedia.summary(directions, 3)
        print(instructions)
        talk(instructions)

    else:
        talk('please repeat the command again.')


while True:
   run_watson()