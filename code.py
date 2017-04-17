from pytg.utils import coroutine
import datetime 
from pytg import Telegram
import time
import json
import sys

tg = Telegram(telegram="tg/bin/telegram-cli",pubkey_file="tg/tg-server.pub")
receiver = tg.receiver
sender = tg.sender
sender.dialog_list()
sender.contacts_list()

MAX = 3
js = {}

def save_js():
	F = open("out_data.txt" , 'w')
	F.write(json.dumps(js))
def getlist ():
	arr = set([])
	F = open("names.txt",'r')
	data = F.readlines()
	for x in data :
		x = x.replace("\n","")
		x = x.replace(" ","")
		print x
		if x[0] == '@':
			arr.add(sender.contacts_search(unicode(x[1:]))['print_name'])
		else :
			arr.add(x)
	print "users"
	for x in arr :
		print "     ",x
	return arr
def make_js(lst):
	print "start.."
	cnt = 0
	while True:
		now = datetime.datetime.now()
		if now.second == 0 :
			cnt+=1
			print "start for ",cnt," time"
			js[str(now)[0:19]] = {}
			for x in lst :
				user = sender.user_info(unicode(x))																													
				try:
					when = user[u'when'][0:19]
					if(str(when) > str(now)):
						js[str(now)[0:19]][x] = ""
				except :
					pass
				time.sleep(1.5)
			if now.minute % 1 == 0:
				print "save"
				save_js()
make_js(getlist())

print json.dumps(js)
