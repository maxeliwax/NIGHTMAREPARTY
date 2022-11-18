-*- coding: utf-8 -*-



import smtplib



# skapar SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
 
# går igenom säkerhet
s.starttls()
 
# Authentication
s.login("max.walldov@gmail.com", "vwymrtkukhcqhgcu")
 
# medelandet du vill skicka 
message = "HEJ skulle du vilja kolla på mitt program "
 
#skickare

motagare=input("vem vill du skicka viruset till ")
s.sendmail("max.walldov@gmail.com", motagare, message)
 
# avslutar
s.quit()







