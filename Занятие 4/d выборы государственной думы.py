parties = {}
allvotes = 0
with open('input.txt', 'r') as f:
	for x in f:
		info = x.split()
		party = ' '.join(info[:-1])
		votes = int(info[-1])
		parties[party] = []
		parties[party].append(votes)
		allvotes += votes

firstquot = allvotes/450
placesleft = 450
for party in parties.keys():
	placescount = parties[party][0]//firstquot
	parties[party].append(placescount)
	parties[party].append(parties[party][0]%firstquot)
	placesleft -= placescount

sortedparties = sorted(parties, key = lambda x: parties[x][2], reverse = True)

for i in range(int(placesleft)):
	parties[sortedparties[i]][1] += 1

for party in parties.keys():
	print(party, int(parties[party][1]))