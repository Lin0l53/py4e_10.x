fname = "mbox-short.txt"
handle = open(fname) 
counter = dict()
for line in handle :
	if line.startswith("From:")  :
		line = line.rstrip()
		#print (line)
		words = line.split()
		sender = words[1]
		pos = sender.find(";")
		email = sender[pos+1:]
		#print (email)
		counter[email] = counter.get(email,0) + 1
	
tmplst = list()

for (k,v) in counter.items(): 
	newt = (v,k)
	tmplst.append(newt)

tmplst = sorted(tmplst, reverse=True)

print ("sorted top 5 :", tmplst[:5])
for v,k in tmplst[:5]:
	print ('#'+str(v),':',k)