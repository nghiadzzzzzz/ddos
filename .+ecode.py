import os
import sys
import time
import random

os.system("clear")
os.system("python .ok.py")

acl='\033[1;30m'
rcl='\033[1;31m'
ycl='\033[1;33m'
ncl='\033[0;00m'
##main
print(ycl+"\n\t Select Your Option :-:")
print(acl+"\n\t[1] Advance Tool Encrypter"+acl+"\n\t[2] Back To Tool-CH "+rcl+"\n\t[0] !! EXIT !!")
opt=str(input(ycl+"\n\n\tEnter Your Option :-: "))

if opt=="1":
   os.system("python .encode.py")

elif opt=="2":
     os.system("python Tool-CH.py")

elif opt=="0":
     sys.exit(ycl+"\n\n\t\t🔰 BYE BYE ")

else:
    print(rcl+"\n\n\tWRONG VALUE ENTERED ")
    time.sleep(1)
    os.system("python .+ecode.py")
