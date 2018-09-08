import math
from functools import reduce

def gcd(m,n):
    x = max(m,n)
    y = min(m,n)
    if x % y == 0:
        return y
    else:
        while x%y!=0:
            z = x %y
            x = y
            y = z
        else:
            return z

def gcd_list(numbers):
    return reduce(lambda x, y: gcd(x,y), numbers)

N, X = map(int, input().split())
x_list = list(map(int, input().split()))

x_list.append(X)

x_list.sort(reverse=True)

if len(x_list) == 1:
    exit()

diffs = []
for i in range(0, N):
    if i == N:
        break
    diff = x_list[i] - x_list[i+1]
    diffs.append(diff)

print(gcd_list(diffs))

