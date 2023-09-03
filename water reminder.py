import win32com.client
import time 
from plyer import notification

title = "WATER REMINDER"
message = "HELLO  KIRTI SHARMA       ITS   TIMES    TO   HYDRATE   PLAESE    DRINK   WATER ."


n = int(input("ENTER THE TIME IN HOURS .. THAT YOU WANT TO  SET REMINDER FOR DRINK WATER AND STAY HYDRATED:  "))
# n = 3600*n

def water_reminder(n):
    for i in range(4):
       
        notification.notify(
    title=title,
    message=message)
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        s = " HELLO  KIRTI SHARMA       ITS   TIMES    TO   HYDRATE   PLAESE    DRINK   WATER  "
        speaker.Speak(s)
        time.sleep(n) 
 
c = int(input("ENTER  00  to start the timer  NOW : "))
if(c== 00):
    water_reminder(n)
else:
    pass


    