N, i, j = map(int, input().split())
sts = abs(j - i) -1
if sts > N - sts -2:
	ans = N - sts - 2
else:
	ans = sts

print(ans)