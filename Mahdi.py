# uncompyle6 version 3.7.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.18 (default, Mar  1 2022, 15:44:46) 
# [GCC Android (7714059, based on r416183c1) Clang 12.0.8 (https://android.google
# Embedded file name: <RED-MAFIA>
# Compiled at: 2022-02-17 23:01:11
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

    r1 = requests.get('https://github.com/Shuvo-BBHH/new-paid/blob/main/mahdi.txt').text
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
