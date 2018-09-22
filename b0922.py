N, M, A, B = map(int, input().split())

nums = []

for i in range(0,N):
    nums.append(B)

#print(nums)

for i in range(0,M):
    L, R = map(int, input().split())
    for j in range(L-1, R):
        nums[j] = A

ans = 0
for i in range(0,N):
    ans += nums[i]

#print(nums)

print(ans)
