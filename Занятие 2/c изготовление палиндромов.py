string = input()
counter = 0
m = len(string)//2
for i in range(m):
	if string[i] != string[-1-i]:
		counter +=1 
print(counter)