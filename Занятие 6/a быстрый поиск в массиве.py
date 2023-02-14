n = int(input())
array = sorted(list(map(int, input().split())))
k = int(input())

def leftbinsearch(l, r, array, num):
	while l < r:
		m = (r + l) // 2
		if array[m] >= num:
			r = m
		else:
			l = m + 1
	return l
def rightbinsearch(l, r, array, num):
	while l != r:
		m = (r+l+1)//2
		if array[m] <= num:
			l = m 
		else:
			r = m - 1
	return l
ans = []
for i in range(k):
	left, right = map(int, input().split())
	if left > array[-1]:
		ans.append(0)
	elif right < array[0]:
		ans.append(0)
	else:
		rightpos = rightbinsearch(0, len(array) - 1, array, right)
		leftpos = leftbinsearch(0, len(array) - 1, array, left)
		ans.append(rightpos - leftpos + 1)

print(*ans)