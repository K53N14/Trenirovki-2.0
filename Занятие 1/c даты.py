x, y, z = map(int, input().split())

if x <= 12 and y <= 12 and x != y:
	ans = 0
else:
	ans = 1

print(ans)