import random

import pyupm_grove as grove
import pyupm_buzzer as upmBuzzer
import pyupm_i2clcd as lcd

button = grove.GroveButton(4)

if button.



while 1:
    
    if button.value():
      print("Prueba")

del button