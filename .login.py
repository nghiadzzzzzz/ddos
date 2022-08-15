import getpass
import hashlib
import sys
import os
#---c_value--
acl='\033[1;30m'
rcl='\033[1;31m'
ycl='\033[1;33m'
ncl='\033[0;00m'

password = getpass.getpass()

filepass = open("/data/data/com.termux/files/usr/share/login/.pass", "r")
filepass = filepass.read().split("\n")[0]

password = password.encode()
password = hashlib.sha1(password).hexdigest()

if password != filepass:
    print(rcl+"Invalid password")
    os.system("exit")
else:
    prefix = "/data/data/com.termux/files/usr"
    home = "/data/data/com.termux/files/home"
    motd = False
    hush = False

    os.system("clear")

    try:
        open(prefix + "/etc/motd")
        motd = True
    except:
        motd = False

    try:
        open(home + "/.hushlogin")
        hush = True
    except:
        hush = False

    if motd and not hush:
        print(open(prefix + "/etc/motd").read())
    
    os.system(sys.argv[1] + " " + sys.argv[2])
