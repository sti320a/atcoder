N, M, Q = map(int, input().split())

LR = []
for m in range(0, M):
    L, R = map(int, input().split())
    LR += [[L,R]]

pq = []
for q in range(0, Q):
    p, q = map(int, input().split())
    pq += [[p,q]]

#print(LR)
#print(pq)


for p, q in pq:
    j = 0
    for l, r in LR:
        #print("p, q = " + str(p) +","+str(q))
        #print("l, r = " + str(l) +","+str(r))
        if p <= l and r <= q:
            j += 1
    print(j)