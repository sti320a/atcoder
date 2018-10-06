N, M = map(int, input().split())

if N % M == 0:
    print(N/M)
    exit()

if N % M != 0:
    print(N % M)


