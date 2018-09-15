N, x = map(int, input().split())
a_list = list(map(int, input().split()))


a_list = sorted(a_list, reverse=False)

ans = 0
for num in a_list:
    x = x - num
    if x >= 0:
        ans += 1
    else:
        break

if x > 0:
    ans -= 1
elif x <= 0:
    pass
    

print(ans)
