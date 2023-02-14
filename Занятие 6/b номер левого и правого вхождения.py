n = int(input())
array = sorted(list(map(int, input().split())))
m = int(input())
nums = list(map(int, input().split()))

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

for i in range(m):
	num = nums[i]
	if num not in array:
		print('0 0')
	else:
		rightpos = rightbinsearch(0, len(array) - 1, array, num)
		leftpos = leftbinsearch(0, len(array) - 1, array, num)
		print(leftpos + 1, rightpos + 1)