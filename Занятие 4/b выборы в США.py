candidates = {}
with open('input.txt', 'r') as f:
	for x in f:
		candidate, votes = x.split()
		votes = int(votes)
		if candidate not in candidates.keys():
			candidates[candidate] = 0
		candidates[candidate] += votes 
sortedkeys = sorted(candidates.keys())
for key in sortedkeys:
	print(key, candidates[key])