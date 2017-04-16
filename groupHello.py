from pytg.receiver import Receiver
from pytg.utils import coroutine
import datetime 
from pytg import Telegram
import time
import json

tg = Telegram(telegram="tg/bin/telegram-cli",pubkey_file="tg/tg-server.pub")
receiver = tg.receiver
sender = tg.sender
group = "INOI26"

@coroutine
def example_function(receiver):
	s= set ([])
	while True:
		msg = (yield)
		try :
			
			if msg['peer']['name']==group:
				if str(msg['sender']['name']) not in s:
					s.add(str(msg['sender']['name']))
					sender.reply(msg['id'],"Salam "+msg['sender']['first_name'])
		except :
			pass
receiver.start()  # start the Connector.
receiver.message(example_function(receiver))  # add "example_function" function as listeners. You can supply arguments here (like receiver).
# continues here, after exiting while loop in example_function()
receiver.stop()
