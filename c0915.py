N, X = map(int, input().split())
x_list = list(map(int, input().split()))


base = N * X + X

x_list = sorted(x_list, reverse=True)

var = 0
k = 0