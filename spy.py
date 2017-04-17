import json 

data = json.load(open('fff.txt','r'))	
for x in data: 
	for y in data[x]:
		print y
