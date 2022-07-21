import pyttsx3
import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)  # apply voice choice
engine.say('welcome back, how may i assist you') # start up voice line
# engine.say('how may i help')
# v in voices:
# print(v)

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
        song = command.replace('play', '')  # replace "play" from command and take only song name
        talk('playing' + song)  # have watson say "playing" and the song name taken from prior line
        pywhatkit.playonyt(song)  # play said song on YouTube

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        talk('the time is ' + time)

    elif 'date' in command:
        date = datetime.date.today().strftime('%b %d %Y')
        talk('today is ' + date)

    elif 'who' in command:
        person = command.replace('who', '')
        info = wikipedia.summary(person, 3)
        print(info)
        talk(info)
    elif 'how do i' in command:
        directions = command.replace('how', '')
        instructions = pywhatkit.info(directions, 3)
        print(instructions)
        talk(instructions)

    elif 'google' in command:
        googlePhrase = command.replace('google', '')
        googleSearch = pywhatkit.search(googlePhrase)
        print(googleSearch)
        talk(googleSearch)

    else:
        talk('please repeat the command again.')


while True:
    run_watson()
