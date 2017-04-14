from pytg.utils import coroutine
import datetime 
from pytg import Telegram
import time

tg = Telegram(telegram="tg/bin/telegram-cli",pubkey_file="tg/tg-server.pub")
receiver = tg.receiver
sender = tg.sender
sender.dialog_list()
sender.contacts_list()

MAX = 10


def getlist ():
	arr = []
	F = open("names.txt",'r')
	data = F.readlines()
	for x in data : 
		arr.append(x)
	return arr
def show_list(lst):
	for TimE in range(MAX):
		time.sleep(1)
		now = datetime.datetime.now()
		print "In Time " , str(TimE) 
		for x in lst :
			user = sender.user_info(unicode(x))
			try:
				when = user[u'when'][0:19]
				if(str(when) > str(now)):
					print "    user" , x , " is online"
				else :
					print "    user" , x , " is offline"
			except :
				pass


show_list(getlist())



#print(sender.user_info(u'Hamidreza'))
#sender.send_msg(u'Sadegh_Mahdavi', u'Hello World!')
