n = int(input())
colorsum = {}
for _ in range(n):
	d, a = map(int, input().split())
	if d not in colorsum.keys():
		colorsum[d] = 0
	colorsum[d] += a 

sortedkeys = sorted(colorsum.keys())

for key in sortedkeys:
	print(key, colorsum[key])