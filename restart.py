import os

restart = input("Do u want to restart ur system ? (y / n) : ")
if restart == 'n':
    exit()
else:
    os.system("shutdown /r /t")
