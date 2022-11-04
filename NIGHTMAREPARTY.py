from plyer import notification
import datetime 
from playsound import playsound
import time
import ctypes
import os
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install("plyer")
install("playsound")
install("ctypes-callable")
  
#play sound
file = "note.mp3"
print('playing sound using native player')
os.system(file)

sec_to_run = 5 
exec_end_time = datetime.datetime.now() +  datetime.timedelta(seconds=sec_to_run) 



 
for i in range(2):
    notification.notify(
        title = 'USER',
        message = 'hej',
        app_icon = 'magda.ico',
        )
    time.sleep(5)





playsound('note.mp3')
print('playing sound using  playsound')



ctypes.windll.user32.SystemParametersInfoW(20,0,"C:\\Users\\maximilian.walldov\\Desktop\\per.jpg", 0)


output = None  

for i in range(6):
    print('hello geek!')
    time.sleep(5)
    if output == None:
        print ("hej1")
        output = 1
    else: 
        print("hej2")
        output = None




    

    




