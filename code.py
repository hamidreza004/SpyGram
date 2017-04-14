from pytg.utils import coroutine
from pytg import Telegram

tg = Telegram(telegram="tg/bin/telegram-cli",pubkey_file="tg/tg-server.pub")
receiver = tg.receiver
sender = tg.sender
def main_loop():
	while not QUIT:
		msg = (yield) 
		print("Message: ", msg)
		# do more stuff here!
		
#
receiver.start()
receiver.message(main_loop())
sender.send_msg("Hamidreza_Hedayati", "Hello World!")
