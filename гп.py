#голосовой ассистент вау
import os
import time
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import datetime

opts = {
   "alias": ('Рина','Ринуша','Рини','Рин'),
   "tbr": ('скажи', 'расскажи', 'покажи', 'сколько','произнеси'),
   "cmds": {
      "ctime": ('текущее время','сейчас времени','который час'),
      "radio": ('включи музыку','воспроизведи радио','включи радио'),
      "stupid1": ('расскажи анекдот','рассмеши меня','ты знаешь какой-нибудь анекдот?')
   }
}
#функции
def speak(what):
   print( what )
   speak_engine.say( what )
   speak_engine.runAndWait()
   speak_engine.stop()

def callback(recognizer, audio):
   try:
      voice = recognizer.recognize_google(audio, language = "ru-RU").lower()
      print("[log] Распознано: " + voice)
   
      if voice.startswith(opts["alias"]):
         cmd = voice

         for x in opts['alias']:
            cmd = cmd.replace(x, "").strip()

         for x in opts['tbr']:
            cmd = cmd.replace(x, "").strip()

         cmd = recognize_cmd(cmd)
         execute_cmd(cmd['cmd'])

   except sr.UnknownValueError:
      print("[log] Голос не распознан! ")
   except sr.RequestError as e:
      print("[log] Неизвестная ошибка, проверьте инет! ")


def recognize_cmd(cmd):
   RC = {'cmd': '', 'percent': 0}
   for c,v in opts['cmds'].items():

      for x in v:
         vrt = fuzz.ratio(cmd, x)
         if vrt > RC['percent']:
            RC['cmd'] = c
            RC['percent'] = vrt

def execute_cmd(cmd):
   if cmd == 'ctime':
      now = datetime.datetime.now()
      speak("Сейчас " + str(now.hour) + ":" + str(now.minute))

   elif cmd == 'stupid1':
      speak(" Пришёл как то негр к врачу и говорит ему у меня очень болит рот. ну врач ему и говорит раздевайтесь и вставай на четвереньки. ну сделал негр все что врач просил, и врач ему говорит теперь ползите в этот угол. негр пополз.сейчас ползите в тот. короче лазил-лазил негр по полу на четвереньках, и решает спросить врача а это что какая то новая методика лечения?.а врач ему и отвечает да я просто стол чёрный хочу купить, вот смотрю где лучше поставить ")

   else:
      print('Команда не распознана, повторите!')

#запуск
r = sr.Recognizer()
m = sr.Microphone(device_index = 1)

with m as source:
   r.adjust_for_ambient_noise(source)

speak_engine = pyttsx3.init()


speak("Приветики")
speak("Рина слушает")

stop_listening = r.listen_in_background(m, callback)
while True: time.sleep(0.1)