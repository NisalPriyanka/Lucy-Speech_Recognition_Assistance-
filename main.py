from gtts import gTTS
import speech_recognition as str
import os
import webbrowser


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
        command = rec.recognize_google(audio)
        print("you said : ",command)

    except str.UnknownValueError:
        assistant(userCommand())

    return command

#perform execute according to speak command
def assistant(command):
    if 'open' in command:
        #firefox_path = '/usr/lib/firefox-esr/firefox-bin'
        #url = 'https://www.google.lk'
        #webbrowser.get(firefox_path).open(url)
        TalkToMe('Google is Opening')



TalkToMe('I am ready')

while True:

    #infinte loop to wating for next command
    assistant(userCommand())
