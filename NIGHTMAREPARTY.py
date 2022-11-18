from plyer import notification
import datetime 
from playsound import playsound
import time
import ctypes
import subprocess
import webbrowser
import sys




def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install("plyer")
install("playsound")
install("ctypes-callable")
install("rotate-screen")
install("pywin32")


sec_to_run = 5 
exec_end_time = datetime.datetime.now() +  datetime.timedelta(seconds=sec_to_run) 


import time,rotatescreen as rs

pd = rs.get_primary_display()
angle_list = [90, 180, 270, 0]
for i in range(12):
    for x in angle_list:
        pd.rotate_to(x)
        time.sleep(0.5)
 
for i in range(2):
    notification.notify(
        title = 'USER',
        message = 'hej',
        app_icon = 'magda.ico',
        )
    time.sleep(5)





playsound('note.mp3')
print('playing sound using  playsound')
chrome_path = 'C:\\User     s\\maximilian.walldov\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Internet Explorer%s'

webbrowser.get("microsoft edge").open("https://www.bing.com")

for i in range(6):
    time.sleep(5)
    if output == None:
        ctypes.windll.user32.SystemParametersInfoW(20, 0,"C:\\Users\\maximilian.walldov\\test  wallpaper\\image.jpg", 3)
        output = 1
    else: 
        ctypes.windll.user32.SystemParametersInfoW(20, 0,"C:\\Users\\maximilian.walldov\\programering\\NIGHTMAREPARTY\\Surikat.jpg", 3 )
        output = None







    

    




