import requests
import json
import os

def ip():
  print('Введите айпи.')
  ip = input('>>> ')
  response = requests.get('https://ipinfo.io/' + ip + '/json')
  r = response.json()
  try:
    try:
      print('[IP] : ' + r['ip'])
    except:
      pass
    try:
      print('[Страна] : ' + r['country'])
    except:
      pass
    try:
      print('[Регион] : ' + r['region'])
    except:
      pass
    try:
      print('[Город] : ' + r['city'])
    except:
      pass
    try:
      print('[Имя устройства] : ' + r['hostname'])
    except:
      pass
    try:
      print('[Местоположение] : ' + r['loc'])
    except:
      pass
    try:
      print('[Провайдер] : ' + r['org'])
    except:
      pass
    try:
      print('[Часовой пояс] : ' + r['timezone'])
    except:
      pass
    try:
      print('[Почтовый индекс] : ' +  r['postal'])
    except:
      pass
  except Exeption as er:
    print(er)
  print('----------')
  main()

def self_ip():
  response = requests.get('https://ipinfo.io/json')
  r = response.json()
  try:
    try:
      print('[IP] : ' + r['ip'])
    except:
      pass
    try:
      print('[Страна] : ' + r['country'])
    except:
      pass
    try:
      print('[Регион] : ' + r['region'])
    except:
      pass
    try:
      print('[Город] : ' + r['city'])
    except:
      pass
    try:
      print('[Имя устройства] : ' + r['hostname'])
    except:
      pass
    try:
      print('[Местоположение] : ' + r['loc'])
    except:
      pass
    try:
      print('[Провайдер] : ' + r['org'])
    except:
      pass
    try:
      print('[Часовой пояс] : ' + r['timezone'])
    except:
      pass
    try:
      print('[Почтовый индекс] : ' +  r['postal'])
    except:
      pass
  except Exeption as er:
    print(er)
  print('----------')
  main()

def main():
  print('[1] IP пробив')
  print('[2] Собственный IP')
  print('[0] Выход')
  a = input('>>> ')
  if a == '1':
    ip()
  elif a == '2':
    self_ip()
  elif a == '0':
    print('Завершение программы...')
    
  else:
    print('Неверная команда.')
    main()

def clear():
  if os.sys.platform == "win32":
    os.system("cls")
  else:
    os.system("clear")
print("""  _   _ _   _       _ _ _        """)
print(""" | | | | |_(_)     | (_) |_ ___  """)
print(""" | | | | __| |_____| | | __/ _ \ """)
print(""" | |_| | |_| |_____| | | ||  __/ """)
print("""  \___/ \__|_|     |_|_|\__\___| """)
print("""                                 """)
print('Telegram: https://t.me/tl_hack\n')
main()
