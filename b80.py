N = str(input())

sum = 0
for i in range(0,len(N)):
    tmp = int(N[i])
    sum += tmp

if int(N) % sum == 0:
    print("Yes")
else:
    print("No")