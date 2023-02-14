n, q = map(int, input().split())
array = list(map(int, input().split()))

prefsum = [0] * (n + 1)

for i in range(n):
	prefsum[i + 1] = prefsum[i] + array[i]

for i in range(q):
	first, last = map(int, input().split())
	print(prefsum[last] - prefsum[first - 1])