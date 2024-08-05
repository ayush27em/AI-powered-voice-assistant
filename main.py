import speech_recognition as sr 
import webbrowser
import pyttsx3 
import musicLibrary 
import requests
from openai import OpenAI 
from gtts import gTTS 
import pygame 
import os 
import google.generativeai as genai 
import string

genai.configure(api_key="AIzaSyA50zwYQjX_b1xQBy6O3yW1I75ITd4JedY") 
model=genai.GenerativeModel(model_name="gemini-1.5-pro-latest")
recognizer=sr.Recognizer() 
engine=pyttsx3.init() 
newsapi="4019ab8d16334fa3823f3604a598b8ba"

  #pip install pockersphinx 
def speak_old(text):
    engine.say(text)     
    engine.runAndWait() 
def preprocess_sentence(sentence):
    # Create a translation table that maps punctuation characters to None
    translator = str.maketrans('', '', string.punctuation)
    # Remove punctuation from the sentence
    preprocessed_sentence = sentence.translate(translator)
    return preprocessed_sentence
def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running long enough to hear the music
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove("temp.mp3")  
def aiprocess(command):
    client = OpenAI(api_key="sk-proj-hqmWpnBwmzTIsWufqbZYT3BlbkFJBku252bvSmbxLAaoUJ9C")
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are virtual assistant named jarvis skilled in general tasks like alexa and google cloud: give short responses."},
        {"role": "user", "content": command}
    ]
    )

    return print(completion.choices[0].message.content)

def processCommand(c): 
       if "open facebook" in c.lower().strip():
           webbrowser.open("https://facebook.com")
       elif "open google" in c.lower().strip():
           webbrowser.open("https://google.com")
       elif "open youtube" in c.lower().strip():
           webbrowser.open("https://youtube.com") 
       elif c.lower().startswith("play"):
           song=c.lower().split(" ")[1]  
           link=musicLibrary.music[song]
           webbrowser.open(link)    
       elif "news" in c.lower():
           r=requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi} ")
           if r.status_code == 200: 
               #parse the data
               data=r.json() 

               #extract the articles
               articles=data.get('articles',[])

               #now speak all titles from articles
               for article in articles:
                   speak(article['title'])
       else: 
             #let open ai handle the request
             # output=aiprocess(c)  
              #speak(output) 
              response= model.generate_content(command) 
              return speak(preprocess_sentence(response.text) )


if __name__== "__main__":
     speak("initializing Jarvis.... ") 
     while True:  
     #listen for the wake word "jarvis" 
     # obtain audio from the microphone
        r = sr.Recognizer()
        print("recognizing...")
        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
              print("listening....")
              audio = r.listen(source , timeout=2, phrase_time_limit=3) 
              command=r.recognize_google(audio) 
            if(command.lower()== "jarvis"):
                speak("jai shri krishna ") 
                #listen for the comman
                with sr.Microphone() as source:
                 print("jarvis active ")
                 audio = r.listen(source )
                 command=r.recognize_google(audio) 


                processCommand(command)
        except Exception as e:
            print("error;{0}".format(e)) 
        