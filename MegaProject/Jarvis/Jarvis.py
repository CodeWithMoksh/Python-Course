#Modules
import speech_recognition as sr
import webbrowser
import pyttsx3
import requests # This is used for sending the requests and getting the responses from the API


# Recognisers

recogniser = sr.Recognizer() #Used to convert speech into text by processing audio from the microphone or an audio file
engine = pyttsx3.init() #Initializes the text-to-speech engine.


# Response Generator

def processcommand(c):
    if("open google" in c.lower()):
        webbrowser.open("https://google.com")
    elif("open youtube" in c.lower()):
        webbrowser.open("https://youtube.com")
    elif("open github" in c.lower()):
        webbrowser.open("https://github.com")
    elif("open netflix" in c.lower()):
        webbrowser.open("https://netfree.cc")
    elif("news" in c.lower()):
        api_key = "5136d737d45d42b0b1764caa779e1a0a" #This is the API key provided by the dealer of the API. It is special for everyone
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey=5136d737d45d42b0b1764caa779e1a0a" #This is URL from which the API will be getting its resources
        response = requests.get(url) #We send a request to the API
        news_data = response.json() #Convert the response into Python format
        for article in news_data["articles"][:5]: #Printing the News
            print("📰", article["title"])


# Speak Function
def speak(text):
    engine.say(text) #Passes the text to the TTS engine.
    engine.runAndWait() #Processes and plays the speech output.
speak("Initializing Jarvis.....")


# Detecting the Audio Spoken
while True:
    r = sr.Recognizer() #We initialize it again so that it can asks for further questions again and again.

    # Recognizing the recorded audio and converting it to speech
    try:
        with sr.Microphone() as source: #Opens the microphone as an audio input source. It's managed using a with block to handle resources cleanly.
            print("Say something!")
            audio = r.listen(source, timeout=5) #Listens to the audio from your microphone, and stores it in an AudioData object called audio. And timeout here means that this will listen for only 5sec and after it will stop
        
        word = r.recognize_google(audio) #Uses Google's Web Speech API to convert your voice (audio) to a string.

        if(word.lower() == "jarvis"): #If the word came out to be jarvis then jarvis will be activated 
            speak("Yaa I am here for you")
            with sr.Microphone() as source: #Opens the microphone as an audio input source. It's managed using a with block to handle resources cleanly.
                print("Jarvis Activated....")
                
                audio = r.listen(source, timeout=5) #Listens to the audio from your microphone, and stores it in an AudioData object called audio. And timeout here means that this will listen for only 5sec and after it will stop
                command = r.recognize_google(audio)

                processcommand(command)

    except sr.UnknownValueError:
        print("Jarvis could not understand your audio") #This catches the case where speech could not be understood. Maybe background noise, silence, or mumbling.
    
    except Exception as e:
        print("There is an error with the Google API. Try working on your internet connection") #If there's an error communicating with the API (e.g. no internet, service down), this handles it.
