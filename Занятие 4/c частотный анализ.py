wordcount = {}
with open('input.txt', 'r') as f:
	for x in f:
		words = x.strip().split()
		for word in words:
			if word not in wordcount.keys():
				wordcount[word] = 0
			wordcount[word] += 1
sortedkeys = []
for key in wordcount.keys():
	sortedkeys.append((-wordcount[key], key))
sortedkeys.sort()
for value, key in sortedkeys:
	print(key)