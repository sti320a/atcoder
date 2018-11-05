N = int(input())

if N == 1:
    print(1)
elif N == 2:
    print(3)
elif N >= 3:
    prev1 = 1
    prev2 = 3
    for i in range(3, N+1):
        ans = prev1 + prev2
        prev1 = prev2
        prev2 = ans
    print(ans)    
