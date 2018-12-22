import math


N, P = map(int, input().split())

s = 0
while s==0:
    for i in range(2,P+1):
        if P%i==0:
            P=int(P/i)
            if P==1:
                s=1
            print(i)
            break