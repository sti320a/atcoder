import pprint

H, W = map(int, input().split())

box = []

for h in range(1,H+1):
    row = []
    row += list(input())
    box.append(row)

"""
if W == 1 and H == 1:
    print(box[0][0])
    exit()
"""

# 同じ色しかない行
delete_row_num = []
for h in range(0,H):
    row = []
    row += list(box[h])
    if row.count(".") == W:
        delete_row_num.append(h)
        continue

# 同じ色しかない列
delete_col_num = []
for w in range(0,W):
    col = []
    for h in range(0,H):
        col += box[h][w]    
    #if ("#" not in col) or ("." not in col):
    if col.count(".") == H:
        delete_col_num.append(w)
        continue

#print(delete_row_num)
#print(delete_col_num)

for h in range(0,H):
    
    ans = ""
    
    if h in delete_row_num:
        continue

    for w in range(0,W):
        if w in delete_col_num:
            continue
        
        ans += box[h][w]

    print(ans)




#pprint.pprint(box)

