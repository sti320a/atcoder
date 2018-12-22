N, H, W = map(int, input().split())

cnt = 0

for _ in range(0,N):
    A, B = map(int, input().split())
    if H <= A and W <= B:
        cnt += 1  

print(cnt)



