n = int(input())
ans = set(range(1, n+1))
s = input().strip()
while s!= 'HELP':
	guess = set(map(int, s.split()))
	s = input().strip()
	if s == 'YES':
		ans.intersection_update(guess)
	else:
		ans.difference_update(guess)
		
	s = input().strip()
	
print(*sorted(ans))