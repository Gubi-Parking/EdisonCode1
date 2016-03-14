import random

import pyupm_grove as grove
import pyupm_buzzer as upmBuzzer
import pyupm_i2clcd as lcd

button = grove.GroveButton(4)

count = 0;



while 1:
    
    if button.value():
      print("Prueba")
      count+=1
      print(count)

del button