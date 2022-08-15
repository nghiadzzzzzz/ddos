import os
import sys
import time

os.system("python .ok.py")

acl='\033[1;30m'
rcl='\033[1;31m'
ycl='\033[1;33m'
ncl='\033[0;00m'

print(ycl+"\n\n\t Update & Upgradeing...")
os.system("pkg update -y ; pkg upgrade -y")
print(ycl+"PKG's Installing")
os.system("pkg i git -y ; pkg i python -y ; pkg i python2 -y ; pkg i go -y ; pkg i php -y ; pkg i mpv -y ")
print(ycl+"\n\n\t Done ..")
time.sleep(5)
os.system("python Tool-CH.py")
