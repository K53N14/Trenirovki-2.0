def coloredlen(n, lefts, rights):
    events = []
    for i in range(n):
        events.append((lefts[i], rights[i]))
    events.sort()
    ans = 0
    for i in range(len(events)):
        if i == 0:
            ans += events[i][1] - events[i][0]
            right = events[i][1]
        elif events[i][0] > right:
            ans += events[i][1] - events[i][0]
            right = events[i][1]
        elif events[i][1] > right:
            ans += events[i][1] - right
            right = events[i][1]

    return ans
n = int(input())
lefts = []
rights = []
for _ in range(n):
    l, r = map(int, input().split())
    lefts.append(l)
    rights.append(r)

ans = coloredlen(n, lefts, rights)
print(ans)