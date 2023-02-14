parentheses = input().strip()
leftcnt = 0
rightcnt = 0
if parentheses[0] == ')' or parentheses[-1] == '(':
	print('NO')
else:
	for p in parentheses:
		if p == '(':
			leftcnt += 1
		elif p == ')':
			rightcnt += 1

	if leftcnt == rightcnt:
		print('YES')
	else:
		print('NO')