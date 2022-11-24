#impoterar biblotek 
from plyer import notification
import datetime 
from playsound import playsound
import time
import ctypes
import sys
import subprocess


#auto installer
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])



#This makes a timed loop
sec_to_run = 5 
exec_end_time = datetime.datetime.now() +  datetime.timedelta(seconds=sec_to_run) 

#imports and installs libary time and rotate screen
install("rotate-screen")
install("pywin32")

import time,rotatescreen as rs

#rotate primary screen to angle_list 
pd = rs.get_primary_display()
angle_list = [90, 180, 270, 0]
#loop 12 times with 0.5 sec gaps 
for i in range(12):
    for x in angle_list:
        pd.rotate_to(x)
        time.sleep(0.5)
#for loop for notifikation spammer 
install("plyer")
for i in range(5):
    notification.notify(
        #sett title for notifikation 
        title = 'SINGEL.se',
        #the massage you want to send 
        message = 'DIN GRANNE LISA 43 VILL TRÄFFA DIG ',
        #an icom for the notification 
        app_icon = 'magda.ico',
        )
    time.sleep(3)

#play music
install("playsound")

playsound('note.mp3')

install("ctypes-callable")

#sets output to none for the switcher loop
output = None

for i in range(6):
    time.sleep(1)
    if output == None:
        #this will run if output is set to none 
        ctypes.windll.user32.SystemParametersInfoW(20, 0,"C:\\Users\\maximilian.walldov\\test  wallpaper\\image.jpg", 3)
        #sets output to 1 
        output = 1
    else: 
        ctypes.windll.user32.SystemParametersInfoW(20, 0,"C:\\Users\\maximilian.walldov\\programering\\NIGHTMAREPARTY\\Surikat.jpg", 3 )
        output = None