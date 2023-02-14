N = int(input())
seq = list(map(int, input().split()))
time = 0
maxdiploma = seq[0]
for i in range(1, len(seq)):

	if seq[i] > maxdiploma:
		time += maxdiploma
		maxdiploma = seq[i]
	else:
		time += seq[i]

print(time)