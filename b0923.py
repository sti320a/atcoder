N, M, X, Y = map(int, input().split())
XN = list(map(int, input().split()))
YM = list(map(int, input().split()))

if not (X < Y):
    print("War")
    exit()

ymin = min(YM)
xmax = max(XN)

if X == ymin:
    print("War") 
    exit()

if Y == xmax:
    print("War")
    exit()

for x in XN:
    if x >= ymin:
        print("War")
        exit()

print("No War")