a, k, b, m, x = map(int, input().split())
def lbinsearch(l, r, check, checkparams):
	while l<r:
		m = (l+r) // 2
		if check(m, checkparams):
			r = m
		else:
			l = m + 1
	return l 

def checkdays(days, params):
	a, k, b, m, x = params 
	return days * (a + b) - (days//k) * a - (days//m)*b >= x 


ans = lbinsearch(1, x*2, checkdays, (a, k, b, m, x))
print(ans)