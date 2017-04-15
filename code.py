from pytg.utils import coroutine
import datetime 
from pytg import Telegram
import time
import json

tg = Telegram(telegram="tg/bin/telegram-cli",pubkey_file="tg/tg-server.pub")
receiver = tg.receiver
sender = tg.sender
sender.dialog_list()
sender.contacts_list()

MAX = 3
js = {}

def getlist ():
	arr = []
	F = open("names.txt",'r')
	data = F.readlines()
	for x in data :
                if x[0] == '@':                        
                        arr.append(sender.contacts_search(unicode(x[1:]))['print_name'])
                else :
                        arr.append(x[0:(len(x)-1)])
	return arr
def make_js(lst):
	for TimE in range(MAX):
		time.sleep(1)
		js[str(TimE)] = {}
		now = datetime.datetime.now()
		#print "In Time " , str(TimE) 
		for x in lst :
			user = sender.user_info(unicode(x))
			try:
				when = user[u'when'][0:19]
				if(str(when) > str(now)):
                                        js[str(TimE)][x] = "online"
					#print "    user" , x , " is online"
				else :
                                        js[str(TimE)][x] = "offline"
					#print "    user" , x , " is offline"
			except :
				pass


make_js(getlist())
print json.dumps(js)
#print sender.contacts_search(u'Yousef1561')

#print sender.user_info(sender.contacts_search(u'Yousef1561')['print_name'])




#print(sender.user_info(u'Hamidreza'))
#sender.send_msg(u'Sadegh_Mahdavi', u'Hello World!')
