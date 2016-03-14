import random

import pyupm_grove as grove
import pyupm_buzzer as upmBuzzer
import pyupm_i2clcd as lcd
import time

button1 = grove.GroveButton(4)
button2 = grove.GroveButton(3)
count = 0;

check = True
mylcd = lcd.Jhd1313m1(0, 0x3E, 0x62)
mylcd.setColor(0,0,255)


while 1:

  if button1.value() and check:
    mylcd.clear()
    mylcd.setCursor(0,0)
    count +=1
    print(count)
    mylcd.write(str(count))
    check = False
  if button2.value() and check:
    mylcd.clear()
    mylcd.setCursor(0,0)
    count -=1
    print(count)
    mylcd.write(str(count))
    check = False
  elif not(button1.value()) and not(check) and not (button2.value()):
    check = True


del button