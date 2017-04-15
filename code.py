from pytg.utils import coroutine
import datetime 
from pytg import Telegram
import time
import json

tg = Telegram(telegram="tg/bin/telegram-cli",pubkey_file="tg/tg-server.pub")
receiver = tg.receiver
sender = tg.sender
#sender.dialog_list()
#sender.contacts_list()

MAX = 3
js = {}

def save_js():
	F = open("out_data.txt" , 'w')
	F.write(json.dumps(js))

def getlist ():
	arr = []
	F = open("names.txt",'r')
	data = F.readlines()
	for x in data :
		if x[0] == '@':
			arr.append(sender.contacts_search(unicode(x[1:(len(x)-1)]))['print_name'])
		else :
			arr.append(x[0:(len(x)-1)])
	return arr
def make_js(lst):
	while True:
		now = datetime.datetime.now()
		if now.second % 10 == 0:
			js[str(now)[0:19]] = {}
			for x in lst :
				user = sender.user_info(unicode(x))
				try:
					when = user[u'when'][0:19]
					if(str(when) > str(now)):
						js[str(now)[0:19]][x] = "online"
					else :
						js[str(now)[0:19]][x] = "offline"
				except :
					js[str(now)[0:19]][x] = "offline"
			if now.minute % 1 == 0:
				save_js()


make_js(getlist())
print json.dumps(js)



#print sender.contacts_search(u'Yousef1561')

#print sender.user_info(sender.contacts_search(u'Yousef1561')['print_name'])


#print(sender.user_info(u'Hamidreza'))
#sender.send_msg(u'Sadegh_Mahdavi', u'Hello World!')
