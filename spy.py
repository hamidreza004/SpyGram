import json 

data = json.load(open('tmp.txt','r'))	
cnt = 0
zir = 0
for x in data: 
	if (data[x]['Ali_Nademi']=="online" or data[x]['Reyhane_Kharazmipur']=="online"):
		cnt+=1
	if (data[x]['Ali_Nademi']=="online" and data[x]['Reyhane_Kharazmipur']=="online"):
		zir+=1
print zir*100./cnt
