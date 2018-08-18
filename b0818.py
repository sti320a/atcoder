#N = map(int, input().split())
N = int(input())

def getYakusu(N):
    yakusu = 0
    for i in range(1,N+1):
        if N % 2 == 1:
            if N % i == 0:
                yakusu += 1
    return yakusu

ans = 0
for i in range(1,N+1):
    if getYakusu(i) == 8:
        ans += 1

print(ans)
