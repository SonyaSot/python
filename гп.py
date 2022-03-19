from ctypes import addressof
import os
import random
import webbrowser
import speech_recognition
import pyttsx3

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5
speak_engine = pyttsx3.init()
text = ''

commands_dict ={
   'commands': {
   'alias': ['рина','рини','рин','ринуша','друг','чел'],
   'greeting': ['привет','хай','шалом','привет друг'],
   'create_task': ['добавить задачу','создать задачу','черкани задачу','заметка'],
   'play_music': ['включи музыку','дискотека'],
   'brows': ['открой браузер','зайди в инет','открой гугл'],
   'youtube': ['открой youtube','вруби youtube'],
   'web' : ['найди', 'найти']
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
         print('[log] Распознано: ' + query)
      return query
   except speech_recognition.UnknownValueError:
      pass

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
   os.system(f'mpc-hc open {random_file}')

   return f'Танцуем под {random_file.split("/")[-1]}'

def brows():
   webbrowser.open('https://google.ru')

def youtube():
   webbrowser.open('https://youtube.com')

def alias():
   speak('Я тебя слушаю,любезный')
   
   query = listen_command()

def web_search():
   global address
   webbrowser.open('https://yandex.ru/yandsearch?=2028026&text={}&lr=11373'.format(address))

def web():
   global address
   global web_search
   query = listen_command()
   if 'найди' in query:
      address = query.replace('найди','').strip()
      query = query.replace(address, '').strip()
      web_search()
      query = ''
   elif 'найти' in query:
      address = text.replace('найти','').strip()
      text = text.replace(address,'').strip()
      web_search
      text = ''
   address = ''

def main():
   query = listen_command()
   
   for k, v in commands_dict['commands'].items():
      if query in v:
         print(globals()[k]())

while True:
   main()
#if __name__ == '__main__':
   #main()


