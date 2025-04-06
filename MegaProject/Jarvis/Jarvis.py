#Modules:-
import speech_recognition as sr # Converts spoken audio to text.
import webbrowser
import pyttsx3 # Converts text to speech (offline).
import requests # This is used for sending the requests and getting the responses from the API
import cohere # A language model API used to generate text (like ChatGPT).


# Recognisers:-

recogniser = sr.Recognizer() #Used to convert speech into text by processing audio from the microphone or an audio file
engine = pyttsx3.init() #Initializes the text-to-speech engine.


# Speak Function:-

def speak(text):
    engine.say(text) #Passes the text to the TTS engine.
    engine.runAndWait() #Processes and plays the speech output.

speak("Initializing Jarvis.....") #Starting Jarvis


# Response Generator:-

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
    else:
        #If there is nothing like this then we will be generating the response from the Cohere API which is a free platform to use as a alternative to OpenAI API
        co = cohere.ClientV2(api_key="lPfKs4ls1gJexANo59kRZKlf4PNfTKaRprER4U2I")
        res = co.chat(
            model="command-a-03-2025",
            messages=[
                {
                    "role": "user",
                    "content": f"{c} in short",
                }
            ],
        )
        speak(res.message.content[0].text)


# Detecting the Audio Spoken:-

active = True #This variable is used inside the loop from which we can change its value to False in term to stop the loop

while active:
    r = sr.Recognizer() #We initialize it again so that it can asks for further questions again and again.

    # Recognizing the recorded audio and converting it to speech
    try:
        with sr.Microphone() as source: #Opens the microphone as an audio input source. It's managed using a with block to handle resources cleanly.
            print("Say something!")
            audio = r.listen(source, timeout=5) #Listens to the audio from your microphone, and stores it in an AudioData object called audio. And timeout here means that this will listen for only 5sec and after it will stop
        
        word = r.recognize_google(audio) #Uses Google's Web Speech API to convert your voice (audio) to a string.

        if ("stop jarvis" in word.lower()):
            speak("It's been a nice journey with you. Goodbye!")
            active = False #Change the value of the variable to stop the loop
            break

        elif(word.lower() == "jarvis"): #If the word came out to be jarvis then jarvis will be activated 
            speak("Yaa I am here for you")
            with sr.Microphone() as source: #Opens the microphone as an audio input source. It's managed using a with block to handle resources cleanly.
                speak("Jarvis Activated....")
                
                activated = True #Used to end the loop by changing the value to False
                while activated: # There is an another loop in term to make the jarvis continously answering the qustions without activating it again and again
                    audio = r.listen(source, timeout=5) #Listens to the audio from your microphone, and stores it in an AudioData object called audio. And timeout here means that this will listen for only 5sec and after it will stop
                    command = r.recognize_google(audio) #This is a command used to understand the text spoken.

                    if ("stop jarvis" in command.lower()): # This is used to end the loop when stop jarvis is said
                        speak("It's a nice journey with you. Goodbye!")
                        active = False
                        activated = False
                        break # Python’s break always terminates the nearest enclosing loop (like while or for), not the if, else, or try.
                    else:
                        processcommand(command)
        

    except sr.UnknownValueError:
        print("Jarvis could not understand your audio") #This catches the case where speech could not be understood. Maybe background noise, silence, or mumbling.
    
    except Exception as e:
        print("There is an error with the Google API. Try working on your internet connection") #If there's an error communicating with the API (e.g. no internet, service down), this handles it.