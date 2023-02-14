seq = list(map(int, input().split()))
firstset = set()
secondset = set()
ans = []
for i in range(len(seq)):
	if seq[i] not in firstset:
		firstset.add(seq[i])
	elif seq[i] in firstset:
		secondset.add(seq[i])
for i in range(len(seq)):
	if seq[i] not in secondset:
		ans.append(seq[i])
print(*ans)