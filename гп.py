import os
import random
import speech_recognition
import pyttsx3

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5
speak_engine = pyttsx3.init()

commands_dict ={
   'commands': {
   'greeting': ['привет','хай','шалом','привет друг'],
   'create_task': ['добавить задачу','создать задачу','черкани задачу','заметка'],
   'play_music': ['включи музыку','дискотека']
   }
}


def speak(what):
   print( what )
   speak_engine.say( what )
   speak_engine.runAndWait()
   speak_engine.stop()
   

def listen_command():

   try:
      with speech_recognition.Microphone() as mic:
         sr.adjust_for_ambient_noise(source=mic, duration=0.5)
         audio = sr.listen(source=mic)
         query = sr.recognize_google(audio_data=audio, language="ru-RU").lower()
      return query
   except speech_recognition.UnknownValueError:
      return 'Damn...че говоришь :/ ?'

def greeting():
   speak('Приветики чел')
def create_task():
   speak('Что добавим в список дел?')

   query = listen_command()

   with open('todo-list.txt', 'a') as file:
      file.write(f'{query}\n')

   speak(f'Задача {query} добавлена в todo-list!')

def play_music():
   files = os.listdir('music')
   random_file = f'music/{random.choice(files)}'
   os.system(f'xdg-open {random_file}')

   return f'Танцуем под {random_file.split("/")[-1]}'


def main():
   query = listen_command()
   
   for k, v in commands_dict['commands'].items():
      if query in v:
         print(globals()[k]())


if __name__ == '__main__':
   main()


