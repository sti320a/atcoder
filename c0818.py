S = str(input())
K = int(input())


for i in range(0,K):
    if int(S[i]) > 1:
        print(S[i])
        exit()
    print(1)