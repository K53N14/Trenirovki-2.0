seq = []
with open('input.txt', 'r') as f:
	for x in f:
		seq.append(int(x))

maxnum = seq[0]
maxcount = 1
for i in range(1, len(seq)-1):
	if seq[i] == maxnum:
		maxcount += 1
	if maxnum < seq[i]:
		maxnum = seq[i]
		maxcount = 1
	
print(maxcount)