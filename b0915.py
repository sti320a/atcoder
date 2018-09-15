N, X = map(int, input().split())
x_list = list(map(int, input().split()))


base = N * X + X

x_list = sorted(x_list, reverse=True)

var = 0
k = 0

for x in x_list:
    # 端まで移動
    if k == 0:
        var += x
    # 端から次のごみまでの移動エネルギー
    else:
        var += (x_list[k-1] - x_list[k]) * ((k + 1)**2)
    k += 1

# 最後からごみ箱まで
var += (x_list[-1] - 0) * ((k+1)**2)

ans = base + var

print(ans)
