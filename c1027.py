from statistics import mean

N_list = list(map(int, input().split()))
N_list = sorted(N_list, reverse=True)
#[1 2 3 4]

h_len = int(len(N_list) / 2)

big = N_list[0:h_len]
small = N_list[h_len:len(N_list)]

print(big)

small = sorted(small)
print(small)

ans = 0

if len(small) % 2 == 0:
    for i in range(0, len(small)):
        ans += big[i] - small[i]
else:
    for i in range(0, len(big)):
        ans += big[i] - small[i]
        ans