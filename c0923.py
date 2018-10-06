S = str(input())
T = str(input())

bind = []
for i in range(0, len(S)):
    tmp = [S[i], T[i]]
    tmp = sorted(tmp, key=lambda tmp:tmp[0]) 
    bind.append(tmp)

bind = sorted(bind, key=lambda tmp: tmp[0])

print(bind)

for i,row in enumerate(bind):
    if i+1 == len(bind):
        exit()
    if row[0] == bind[i+1][0]:
       if row[1] != bind[i+1][1]:
           print("No")
           exit()

print("Yes")