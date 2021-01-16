from gtts import gTTS               # google text to speech
from time import ctime              # get time details
import speech_recognition as sr     # recognize speech
import playsound                    # to play an audio file
import random
import webbrowser                   # open browser
import time
import os                           # to delete created audio files

class person:
    name = ''
    def setName(self, name):
        self.name = name

def exists(terms):
    for term in terms:
        if term in mic_data:
            return True

r = sr.Recognizer()     # initialize a recognizer

# listen for audio and convert it to text
def record_audio(ask=False):
    with sr.Microphone() as mic:    # microphone as mic
        if ask:
            speak(ask)
        audio = r.listen(mic)       # listen for the audio via mic
        mic_data = ""

        try:
            mic_data = r.recognize_google(audio)    # convert audio to text
        except sr.UnknownValueError:                # error: recognizer does not understand
            speak("I apologize, I did not hear you. Can you please repeat that?")
        except sr.RequestError:
            speak("Sorry, the service is down")     # error: recognizer is not connected


        print(f"Operator: {mic_data.lower()}")      # print what user said
        return mic_data.lower()


# get string and make a audio file to be played
def speak(audio_string):
    tts = gTTS(text=audio_string, lang="en-nz")     # text to speech(voice)
    r = random.randint(1,20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file)                            # save as mp3
    playsound.playsound(audio_file)                 # play the audio file
    print(f"Karen: {audio_string}")                 # print what app said
    os.remove(audio_file)                           # remove audio file


def respond(mic_data):

    # 1: greeting
    if exists(["hey","hi","hello"]):
        greetings = [f"hey, how can I help you {person_obj.name}", f"hey, what's up? {person_obj.name}", f"I'm listening {person_obj.name}", f"how can I help you? {person_obj.name}", f"hello {person_obj.name}"]
        greet = greetings[random.randint(0,len(greetings)-1)]
        speak(greet)

    # 2: name
    if exists(["what is your name","what's your name","tell me your name","who are you"]):

        # checks when there exists a name already
        if person_obj.name:
            speak("My name is Karen")
        else:
            speak("My name is Karen. What's your name?")

    if exists(["my name is"]):
        person_name = mic_data.split("is")[-1].strip()
        speak(f"Okay, I will remember that {person_name}")
        person_obj.setName(person_name) # remember name in person object

    # 3: greeting
    if exists(["how are you","how are you doing"]):
        speak(f"I'm very well, thanks for asking {person_obj.name}")

    # 4: time
    if exists(["what's the time","tell me the time","what time is it", "what is the time"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        meridiem = "am"
        if time[0] == "00":
            hours = "12"
        else:
            hours = str(int(time[0]) % 12)
        if int(time[0]) > 11:
            meridiem = "pm"
        minutes = time[1]
        time = f"It's {hours}:{minutes} {meridiem} CDT"
        speak(time)

    # 5: search google
    if exists(["search"]) and 'youtube' not in mic_data and 'amazon' not in mic_data:
        search_term = mic_data.split("for")[-1]
        url = f"https://google.com/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on google')

    # 6: search youtube
    if exists(["youtube"]):
        remove_text = ["youtube", "on", "in", "search"]
        search_term = mic_data.split("for")[-1]
        
        for text in remove_text:
            if text == "in" or text == "on":
                search_term = search_term.replace(" " + text + " ", "")
            else:
                search_term = search_term.replace(text, "")

        url = f"https://www.youtube.com/results?search_query={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on youtube')

    # 7: search amazon
    if exists(["amazon"]):
        remove_text = ["amazon", "on", "in", "search"]
        search_term = mic_data.split("for")[-1]
        
        for text in remove_text:
            if text == "in" or text == "on":
                search_term = search_term.replace(" " + text + " ", "")
            else:
                search_term = search_term.replace(text, "")

        url = f"https://www.amazon.com/s?k={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on amazon')

    # 8: Turn off the speech assistant
    if exists(["exit", "quit", "goodbye"]):
        speak("going offline")
        exit()

time.sleep(1)

person_obj = person()
while(1):
    mic_data = record_audio()   # get the voice input
    respond(mic_data)           # respond