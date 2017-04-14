from pytg.utils import coroutine
import datetime 
from pytg import Telegram
import time

MAX = 10

def getlist ():
	arr = []
	F = open("names.txt",'r')
	data = F.readlines()
	for x in data : 
		arr.append(x)
	return arr


tg = Telegram(telegram="tg/bin/telegram-cli",pubkey_file="tg/tg-server.pub")
receiver = tg.receiver
sender = tg.sender
sender.dialog_list()
sender.contacts_list()

for i in range(1000):
	sender.send_msg(u'Ali_Ahmadi',u'ine pesar')
sender.send_msg(u'Hamidreza_Hedayati',u'fuck yourself')
