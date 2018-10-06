N, T = map(int, input().split())

kouho = []

for i in range(0, N):
    c, t = map(int, input().split())
    if t <= T:
        kouho.append(c)

if len(kouho) == 0:
    print('TLE')
    exit()

print(min(kouho))            
