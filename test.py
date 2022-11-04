

import datetime 
from plyer import notification 
sec_to_run = 5 
exec_end_time = datetime.datetime.now() +  datetime.timedelta(seconds=sec_to_run) 
 
while True: 
  if datetime.datetime.now() >= exec_end_time: 
    break   
  