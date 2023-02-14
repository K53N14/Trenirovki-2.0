seq1 = set(map(int, input().split()))
seq2 = set(map(int, input().split()))

ans = len(seq1.intersection(seq2))
print(ans)
