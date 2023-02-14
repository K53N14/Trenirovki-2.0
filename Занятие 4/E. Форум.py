n = int(input())
count = 0
topics = {}
for _ in range(n):
	s = int(input())
	if s == 0:
		s = input().strip()
		count += 1
		if s not in topics.keys():
			topics[s] = []
		topics[s].append(count)
		s = input()
	else:
		count += 1
		for key in topics.keys():
			if s in topics[key]:
				topics[key].append(count)
		s = input()

maxval = 0

for key in topics.keys():
	if len(topics[key]) > maxval:
		maxval = len(topics[key])

for key in topics.keys():
	if len(topics[key]) == maxval:
		print(key)
		break
