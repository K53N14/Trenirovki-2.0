L, K = map(int, input().split())
seq = list(map(int, input().split()))

if L//2 in seq and L%2 == 1:
	print(L//2)
else:
	for s in seq:
		if s < L//2:
			left = s
		if s >= L//2:
			right = s
			break

	print(left, right)