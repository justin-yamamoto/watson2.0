import pyttsx3
import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)  # apply voice choice
# engine.say('welcome back, how may I assist you')  # start up voice line


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
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'google' in command:
        googlePhrase = command.replace('google', '')
        pywhatkit.search(googlePhrase)

    elif 'are you there' in command:
        talk('i am here')

    elif 'how are you' in command:
        talk('i am swell thank you for asking')

    elif 'can you hear me' in command:
        talk('i can hear you')

    elif 'who is your creator' in command:
        talk('justin yamamoto created me')

    else:
        talk('please repeat the command again.')


while True:
    run_watson()
