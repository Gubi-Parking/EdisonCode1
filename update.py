from firebase import firebase
import pyupm_grove as grove
import pyupm_buzzer as upmBuzzer
import pyupm_i2clcd as lcd
import time
import thread

def update(threadName,firebase,count):
  firebase.patch('/ITESM/Zone1', {'Busy':count})

#define the firebase database from which the program will be working
firebase = firebase.FirebaseApplication('https://gubi.firebaseio.com', None)
#count is equals to the property in the database "lugares"
count=firebase.get('/ITESM/Zone1/Busy', None)
total=firebase.get('/ITESM/Zone1/Total', None)
#define the buttons connected to the intel edison
button1 = grove.GroveButton(4)
button2 = grove.GroveButton(3)
button1b = grove.GroveButton(5)
button2b = grove.GroveButton(6)

#initialization of our variables
check = True #to avoid measuring press and hold
checkb=True #to avoid measuring press and hold
pressed=False #this way we can determine if a button was already pressed
same1=False #in case the same button has been pressed
same2=False #in case the same button has been pressed
pressedb=False #this way we can determine if a button was already pressed
same1b=False #in case the same button has been pressed
same2b=False #in case the same button has been pressed
mylcd = lcd.Jhd1313m1(0, 0x3E, 0x62) #make mylcd reference the lcd screen connected
mylcd.setColor(0,255,0) #set color of lcd screen to blue
mylcd.clear() #clear the screen from any info printed before
mylcd.setCursor(0,0) #set cursor at the first character space
mylcd.write(str(count)) #write the count retrieved from firebase


while 1:

  if button1.value() and check: #if button is pressed and it's not the case of a press and hold
    check = False #check changes to false to avoid a press and hold
    if same1: #if it was pressed twice in a row, it changes the values back to normal
      same1=False 
      pressed=False
    elif pressed and not (same1): #if it's the second press and it's not the same button twice
      count+=1 #count increases since a car entered the zone
      pressed= False #pressed goes back to default
      same2=False #we reset the opposite same
      mylcd.clear()
      mylcd.setCursor(0,0)
      #we use a thread to update the database so locally the intel edison can still change its own value.
      #we do this to prevent the intel edison from getting stuck on the update possibly
      try:
        thread.start_new_thread( update, ("Thread-1",firebase,count ) )
      except:
        print "Error: unable to start thread"

    else:
      #this case is the first press
      pressed=True
      same1=True
  if button2.value() and check:
    #the button has been pressed and it's not the case of a press and hold
    check = False #change the value of check to avoid it checking a press and hold
    if same2: #if the same button has been pressed twice in a row
      same2=False  #change same back to false
      pressed=False #and pressed as well
    elif pressed and not(same2): #if it's the second button to be pressed and it's not twice in a row
      count-=1 #decrease the number of cars since the car that passed was heading outside the zone
      pressed= False #reset the pressed
      same1=False #and the same1
      mylcd.clear()
      mylcd.setCursor(0,0)
      #thread used for update of the firebase database
      try:
        thread.start_new_thread( update, ("Thread-2",firebase,count ) )
      except:
        print "Error: unable to start thread"
    else:
      #if it was the first press, then we change pressed and same2 to one
      pressed=True
      same2=True
  elif not(button1.value()) and not(check) and not (button2.value()):
    check = True
    #change check to true whenever the button has been released

  

  #Other bump


  if button1b.value() and checkb: #if button is pressed and it's not the case of a press and hold
    checkb = False #check changes to false to avoid a press and hold
    if same1b: #if it was pressed twice in a row, it changes the values back to normal
      same1b=False 
      pressedb=False
    elif pressedb and not (same1b): #if it's the second press and it's not the same button twice
      count+=1 #count increases since a car entered the zone
      pressedb= False #pressed goes back to default
      same2b=False #we reset the opposite same
      mylcd.clear()
      mylcd.setCursor(0,0)
    
      
      #we use a thread to update the database so locally the intel edison can still change its own value.
      #we do this to prevent the intel edison from getting stuck on the update possibly
      try:
        thread.start_new_thread( update, ("Thread-1",firebase,count ) )
      except:
        print "Error: unable to start thread"

    else:
      #this case is the first press
      pressedb=True
      same1b=True
  if button2b.value() and checkb:
    #the button has been pressed and it's not the case of a press and hold
    checkb = False #change the value of check to avoid it checking a press and hold
    if same2b: #if the same button has been pressed twice in a row
      same2b=False  #change same back to false
      pressedb=False #and pressed as well
    elif pressedb and not(same2b): #if it's the second button to be pressed and it's not twice in a row
      count-=1 #decrease the number of cars since the car that passed was heading outside the zone
      pressedb= False #reset the pressed
      same1b=False #and the same1
      mylcd.clear()
      mylcd.setCursor(0,0)
 
      #thread used for update of the firebase database
      try:
        thread.start_new_thread( update, ("Thread-2",firebase,count ) )
      except:
        print "Error: unable to start thread"
    else:
      #if it was the first press, then we change pressed and same2 to one
      pressedb=True
      same2b=True
  elif not(button1b.value()) and not(checkb) and not (button2b.value()):
    checkb = True
    #change check to true whenever the button has been released

  if count<total/2:
    
    mylcd.setColor(0,255,0)

  elif count>total/2 and count<(total-5):
    #all necesarry stuff to print on the lcd screen the count
    mylcd.setColor(255,255,0)
    

  elif count>(total-5):
    mylcd.setColor(255,0,0)
  
  if total-count>0:

    mylcd.write(str(total-count))

  else:
    mylcd.write("Max capacity!!1!")

    
del button1
del button2
del button1b
del button2b