import sys 
A, B, K = map(int, input().split())

for i in range(0,K):
    
    if i % 2 == 0:
        if A % 2 == 1:
            A -= 1

        B += int(A / 2)
        A -= int(A / 2)

    else:
        if B % 2 == 1:
            B -= 1

        A += int(B / 2)
        B -= int(B / 2)

print(str(A) + " " + str(B))
    