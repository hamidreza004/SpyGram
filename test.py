import datetime

while True :
	now = datetime.datetime.now()
	if now.second % 30 == 0 :
		print now.second
