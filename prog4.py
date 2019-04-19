words = ['ketul' , 'deepak' , 'tejas']

for i in range(len(words)-1):
	#print("the largest word is",words[i] if len(words[i]) > len(words[i+1]) else print words[i+1]
	if len(words[i]) > len(words[i+1]):
		largest = words[i]

	else:
		largest = words[i+1]
print largest
