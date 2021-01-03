import os

shutdown = input("Do u want to shutdown ur system ? (y / n) : ")
if shutdown == 'n':
    exit()
else:
    os.system("shutdown /s /t")
