#holan omeed AI
import pyttsx3  # converts text to speech
import datetime  # required to resolve any query regarding date and time
import speech_recognition as sr  # required to return a string output by taking microphone input from the user
import wikipedia  # required to resolve any query regarding wikipedia
import webbrowser  # required to open the prompted application in web browser
import os.path  # required to fetch the contents from the specified folder/directory
import smtplib  # required to work with queries regarding e-mail
import pywhatkit
import pyjokes
import wolframalpha
import requests

name = 'vera'

engine = pyttsx3.init(
    'sapi5')  # sapi5 is an API and the technology for voice recognition and synthesis provided by Microsoft
voices = engine.getProperty('voices')  # gets you the details of the current voices
engine.setProperty('voice', voices[1].id)  # 0-male voice , 1-female voice


def speak(audio):  # function for assistant to speak
    engine.say(audio)
    engine.runAndWait()  # without this command, the assistant won't be audible to us


def wishme():  # function to wish the user according to the daytime
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning')

    elif hour > 12 and hour < 18:
        speak('Good Afternoon')

    else:
        speak('Good Evening')

    speak(f'Hello Sir, I am {name}, your Artificial intelligence assistant holan. Please tell me how may I help you'),(name)
    #speak(name)
    #speak(', your Artificial intelligence assistant holan. Please tell me how may I help you')


def takecommand():  # function to take an audio input from the user
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 2
        audio = r.listen(source)

    try:  # error handling
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')  # using google for voice recognition
        print(f'User said: {query}\n')

    except Exception as e:
        print('Say that again please...')  # 'say that again' will be printed in case of improper voice
        return 'None'
    return query


def sendemail(to, content):  # function to send email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('holandeveloper@gmail.com', '@Holan2002')
    server.sendmail('holandeveloper@gmail.com', to, content)
    server.close()


if __name__ == '__main__':  # execution control
    wishme()
    while True:
        query = takecommand().lower()  # converts user asked query into lower case

        # The whole logic for execution of tasks based on user asked query
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=5)
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif "who made you" in query or "who created you" in query:
            speak("I have been created by holan.")
        elif 'play music' in query:
            speak('okay boss')
            music_dir = 'music_dir_of_the_user'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif "calculate" in query:

            app_id = "RPUVH4-9G66YJGRQ4"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)
        elif 'power point presentation' in query:
            speak("opening Power Point presentation")
            power = r"C:"
            os.startfile(power)
        elif "Question "in query:

            app_id = "RPUVH4-9G66YJGRQ4"
            client = wolframalpha.Client(app_id)
            #indx = query.lower().split().index('calculate')
            #query = query.split()[indx + 1:]
            print("what is your question?")
            speak("what is your question?")
            q=takecommand()
            res = client.query(q)
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)
        elif 'what is love' in query:
            speak("It is 7th sense that destroy all other senses")
        elif 'time' in query:
            strtime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'Sir the time is {strtime}')


        elif 'open stack overflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'open free code camp' in query:
            webbrowser.open('freecodecamp.org')

        elif 'pycharm' in query:
            codepath = 'pycharm_directory_of_your_computer'
            os.startfile(codepath)

        elif 'email' in query:
            try:
                speak('what should i write in the email?')
                content = takecommand()
                to = 'iborasul@gmail.com'
                sendemail(to, content)
                speak('email has been sent')
            except Exception as e:
                print(e)
                speak('Sorry, I am not able to send this email')
        elif "write a note" in query:
            speak("What should i write, sir")
            note = takecommand()
            file = open('test.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takecommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
        elif "weather" in query:

            # Google Open weather website
            # to get API of Open weather
            api_key = "YOUR_API_KEY"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            speak(" City name ")
            print("City name : ")

            city_name = takecommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()

            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in celsius unit) = " + str(
                    current_temperature-273.15) + "\n atmospheric pressure (in hPa unit) =" + str(
                    current_pressure) + "\n humidity (in percentage) = " + str(
                    current_humidiy) + "\n description = " + str(weather_description))
                speak(" Temperature (in celsius unit) = " + str(
                    current_temperature-273.15) + "\n atmospheric pressure (in hPa unit) =" + str(
                    current_pressure) + "\n humidity (in percentage) = " + str(
                    current_humidiy) + "\n description = " + str(weather_description))
            else:
                speak(" City Not Found ")
        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))
        elif 'change name' in query:
            print("what name you want to call me")
            speak("what name you want to call me")
            name=takecommand()
            speak(f"my name now is {name}")
        elif 'what is your name' or 'what\'s your name' in query:
            speak(f'my name is {name}')
        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'open power point presentation' in query:
            speak("opening Power Point presentation")
            power = r"filePath"
            os.startfile(power)
        elif 'exit' or 'done' in query:
            speak('okay boss, please call me when you need me')
            quit()

