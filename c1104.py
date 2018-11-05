from collections import defaultdict

N, M = map(int, input().split())

py_dict = defaultdict(list)
for i in range(0,M):
    P, Y = map(int, input().split())
    py_dict[P].append(Y)


sorted(py_dict.items())
s
for n in range(0,N):
    P = n+1
    py_dict
    for y in py_dict[n+1]:
        print(str(P)+"-"+str(y))