
from firebase import firebase
import pyupm_grove as grove
import pyupm_buzzer as upmBuzzer
import pyupm_i2clcd as lcd
import time
import thread

def update(threadName,firebase,count):
  firebase.patch('/ITESM/Zone1', {'Lugares':count})


firebase = firebase.FirebaseApplication('https://gubi.firebaseio.com', 
None)
count=firebase.get('/ITESM/Zone1/Lugares', None)



button1 = grove.GroveButton(4)
button2 = grove.GroveButton(3)


check = True
pressed=False
same1=False
same2=False
mylcd = lcd.Jhd1313m1(0, 0x3E, 0x62)
mylcd.setColor(0,0,255)
mylcd.clear()
mylcd.setCursor(0,0)
mylcd.write(str(count))

while 1:

  if button1.value() and check:
    check = False
    if same1:
      same1=False
      pressed=False
    elif pressed and not (same1):
      count+=1
      pressed= False
      same2=False
      mylcd.clear()
      mylcd.setCursor(0,0)
      mylcd.write(str(count))
      
      try:
        thread.start_new_thread( update, ("Thread-1",firebase,count ) )
      except:
        print "Error: unable to start thread"

    else:
      pressed=True
      same1=True
  if button2.value() and check:

    check = False
    if same2:
      same2=False  
      pressed=False
    elif pressed and not(same2):
      count-=1
      pressed= False
      same1=False
      mylcd.clear()
      mylcd.setCursor(0,0)
      mylcd.write(str(count))
      try:
        thread.start_new_thread( update, ("Thread-2",firebase,count ) )
      except:
        print "Error: unable to start thread"
    else:
      pressed=True
      same2=True
  elif not(button1.value()) and not(check) and not (button2.value()):
    check = True
    
    
del button
