fname = input("Please enter file name :")
if len(fname) < 1 :
	fname = "mbox-short.txt"
fhandle = open(fname)
hoursofday = {}
for line in fhandle :
	line = line.lstrip()
	if not line.startswith("From "): continue 
	#print(line)
	time = line.split()[5]
	hour = time.split(':')[0]
	hoursofday[hour] = hoursofday.get(hour,0) +1
lst = list(hoursofday.items())
lst.sort()
for t in lst :
	print(t[0],t[1])
	

