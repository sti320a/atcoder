import collections

n = int(input())
v_list = list(map(int, input().split()))

A = []
B = []
for i, v in enumerate(v_list):
    if i % 2 == 0:
        A.append(v)
    else:
        B.append(v)


A_co = collections.Counter(A).most_common()
B_co = collections.Counter(B).most_common()

print(A_co)
print(B_co)

X = A_co[0][0]
X_num = A_co[0][1]

Y = B_co[0][0]
Y_num = B_co[0][1]

