import os #for passing command
import pygame #for executing our audio
#You Also Need To Install EdgeTTS Module


os.system("cls") #for clearing console 

print("Welcome To Dhuani ध्वनि (Text to Speech.\n")
FunFacts=["You can also select languages by typing 'hi' for hindi and 'en' for english!","This programm is written by snip in one of his practice programms."]

# speak function that Uses EdgeTTS to save audio file as data.py, then execute it using  pygame(+pyaudio)
def speak(data):

    command=f'edge-tts --rate=-15% --voice "{voice}" --text "{data}" --write-media "Dhuani/data.mp3"'
    os.system(command)
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("Dhuani/data.mp3")
    try:
     pygame.mixer.music.play()

     while pygame.mixer.music.get_busy():
         pygame.time.Clock().tick(10)
    except Exception as e:
     print("\nSomething went wrong internally :(\n",e)
    finally:
     pygame.mixer.music.stop()
     pygame.mixer.quit()
  

while True:
  Userlang=input("Enter Your Speech Language (Hindi & English):").lower()
  if Userlang == "hindi" or Userlang == "hi":
    voice="hi-IN-MadhurNeural"
  if Userlang== "english" or Userlang == "en":
    voice="en-US-SteffanNeural"
  Userinput=input("Enter Your Query:\n")
  speak(Userinput)
 




     





