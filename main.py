# ******************************
# Make your Code
# ******************************

names = input('Enter 5 students names').split()

for i in range(len(names)):
	if i == 0 or minlen > len(names[i]):
		minlen = len(names[i])
		minidx = i
	elif minlen == len(names[i]) and names[i] < names[minidx]:
		minlen = len(names[i])
		minidx = i

	if i == 0 or maxlen < len(names[i]):
		maxlen = len(names[i])
		maxidx = i
	elif maxlen == len(names[i]) and names[i] < names[maxidx]:
		maxlen = len(names[i])
		maxidx = i

print (names[minidx], names[maxidx])

	
