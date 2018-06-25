from gtts import gTTS
import speech_recognition as str
import os
import webbrowser
#from brain_lucy import brain_lucy
import subprocess


# function to make programme talk
def TalkToMe(audio):
    print(audio)
    tts = gTTS(text=audio, lang='en')
    tts.save('audio.mp3') #save the audio to speak same directory we working
    os.system('mpg123 audio.mp3') #play the audio

def userCommand():
    rec = str.Recognizer() #assign recogizer to 'rec' varaible to use later

    #use mic and store given voice commands in source variable
    with str.Microphone() as source:
        print("I am ready for your commands")
        rec.pause_threshold=1

        #reducing background noise when taking
        rec.adjust_for_ambient_noise(source, duration=1)

        #store filtered mic_audio in audio variable
        audio = rec.listen(source)

    try:
        #convert analog audio to String using recognise google function
        global command
        command = rec.recognize_google(audio)
        print("you said : ", command)

    except str.UnknownValueError:
        assistant(userCommand())

    return command

#perform execute according to speak command
def assistant(command):
    if 'open' in command:
         TalkToMe('What do you want me to open?')
         url = userCommand()
         if 'Google' in url:
             os.system('firefox-esr https://www.google.lk')
             TalkToMe('I am opening firefox')

    if 'who are you' in command:
         whoami = subprocess.check_output("whoami", shell=True)
         TalkToMe("Hello "+whoami+", My Name is Lucy. I am your personal assistance. I can answer your questions, Help you to manage your computer, Remember your important stuffs. Please consider me as your best friend.")
    




TalkToMe('I am ready')

while True:

    #infinte loop to wating for next command
    assistant(userCommand())
