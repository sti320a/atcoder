N = input()
T, A = map(int, input().split())
Hs = list(map(int, input().split()))

result1 = []
for x in Hs:
    tmp = T - (x * 0.006)
    result1.append(tmp)

result2 = {}
for i, tmp in enumerate(result1):
    result2[i+1] = abs(A - tmp)


print(sorted(result2.items(), key=lambda x: x[1])[0][0])

