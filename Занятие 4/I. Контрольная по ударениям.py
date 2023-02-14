def addword(wordict,word):
	lowerword = word.lower()
	if lowerword not in wordict.keys():
		wordict[lowerword] = []
	wordict[lowerword].append(word)

N = int(input())
wordict = {}
for _ in range(N):
	word = input().strip()
	addword(wordict, word)

text = input().split()
ans = 0
for word in text:
	if word.lower() in wordict:
		if word not in wordict[word.lower()]:
			ans += 1
	elif word.islower():
		ans += 1
	else:
		upperchar = 0
		for char in word:
			if char.isupper():
				upperchar += 1
		if upperchar > 1:
			ans += 1
print(ans)




