import random

import pyupm_grove as grove
import pyupm_buzzer as upmBuzzer
import pyupm_i2clcd as lcd

button = grove.GroveButton(3)


myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)

while 1:
    count = 0
    myLcd.setCursor(0, 0)
    myLcd.write(count);
    
    if button.value():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        myLcd.setColor(r, g, b)
        buzzer.playSound(chords[ran])
        count = count +1

del button