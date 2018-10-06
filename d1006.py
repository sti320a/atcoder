N, M = map(int, input().split())

if M % N == 0:
    print(int(M/N))
    exit()

if M % N != 0:
    print(M % N)
