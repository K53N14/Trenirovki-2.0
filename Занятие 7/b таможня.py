def ammountofmachines(n, arrival, process):
    events = []
    for i in range(n):
          events.append((arrival[i], 1))
          events.append((arrival[i] + process[i], -1))
    events.sort()
    quantity = 0
    bestquantity = 0
    for i in range(len(events)):
        if events[i][1] == 1:
            quantity += 1
        else:
            quantity -= 1
        if bestquantity < quantity:
             bestquantity = quantity
    return bestquantity
n = int(input())
arrival = []
process = []
for _ in range(n):
    t, l = map(int, input().split())
    arrival.append(t)
    process.append(l)
ans = ammountofmachines(n, arrival, process)
print(ans)