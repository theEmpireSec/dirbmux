import os
import sys
import requests
import threading
from colorama import Fore
os.system('clear')
banner  = Fore.LIGHTMAGENTA_EX+'''

     _ _       _                       
    | (_)     | |                      
  _ | |_  ____| | _  ____  _   _ _   _ 
 / || | |/ ___) || \|    \| | | ( \ / )
( (_| | | |   | |_) ) | | | |_| |) X ( 
 \____|_|_|   |____/|_|_|_|\____(_/ \_)
                                       
Author    : king
Instagram : @the.empiresec
GitHub    : https://github.com/theEmpireSec
'''
print(banner)
print()
print(Fore.LIGHTRED_EX+"[+] Enumeration started \n[!] Starting threads....\n")
def check(url):
	if url.startswith("http://") is False:
		url = "http://" + url
	try:
		if requests.get(url):
			print(Fore.LIGHTCYAN_EX+"[+] Discoverd -----> " + str(url))
		else:
			pass
	except:
		pass



help = 'python dirbmux.py <url> <pathOfWordlist>'

if len(sys.argv) != 3:
	os.system('clear')
	print(help)
	exit()
arg_url = sys.argv[1]
file = sys.argv[2]
try:
	file = open(file,'r')
except:
	print('File not found :(.......bye bye baby')
	exit()

for word in file.readlines():
	word = word.strip('\n')
	final_url = arg_url + '/' + word
	try:
		t = threading.Thread(target=check,args=(final_url,))
		t.start()
	except KeyboardInterrupt:
		print(Fore.RED+'[!] USER interrupted......bye bye babe\n')
		t.join()
		exit()

print(Fore.RESET+'')
