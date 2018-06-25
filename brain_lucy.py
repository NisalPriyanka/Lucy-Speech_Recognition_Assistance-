import os
import webbrowser
from gtts import gTTS


class brain_lucy:

    def __init__(self, command, cus_commnd):
        self.command = command



    def lucybrain(self):
        if 'open' in self.command:
            print('i am opening google')

    #talking when command is recieved
    def TalkToMe(cus_commnd):
        print(cus_commnd)
        tts = gTTS(text=cus_commnd, lang='en')
        tts.save('audio.mp3')
        os.system('mpg123 audio.mp3')
