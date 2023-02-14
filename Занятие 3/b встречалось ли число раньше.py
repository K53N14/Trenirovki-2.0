seq = list(map(int, input().split()))
prevnums = set()
for i in range(len(seq)):
	if seq[i] not in prevnums:
		print('NO')
		prevnums.add(seq[i])
	else:
		print('YES')