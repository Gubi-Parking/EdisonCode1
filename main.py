import random

import pyupm_grove as grove
import pyupm_buzzer as upmBuzzer
import pyupm_i2clcd as lcd
import time

button = grove.GroveButton(4)
count = 0;

check = True



while 1:

  if button.value():
    print ("Presionado")
    time.sleep(1)
  else:
    print("Suelto")
    time.sleep(1)



del button