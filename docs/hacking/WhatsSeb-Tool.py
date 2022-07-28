#import pywhatkit
#pywhatkit.sendwhatmsg("+59162500018", "Message 2", 15, 17, 15, True, 2)

import pyautogui
import time
import webbrowser as wb

number_of_messages = int(input('Ingrese el número de mensajes: '))
message_content = input('Ingrese el mensaje: ')
number_phone = input('Ingrese el numero de teléfono con el codigo de pais: ') #codpais+n+umero celular

wb.open('https://web.whatsapp.com/send?phone=+'+number_phone)
time.sleep(15)

for num in range(number_of_messages):
    pyautogui.write(message_content)
    pyautogui.press('enter')

print('el mensaje fue enviado satisfactoriamente')
