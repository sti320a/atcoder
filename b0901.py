import math

x1, y1, x2, y2 = map(int, input().split())

#2点間の距離を求める
def getDistance(x_1, y_1, x_2, y_2):
    result2 = pow(x_2 - x_1, 2) + pow(y_2 - y_1, 2)
    result = math.sqrt(result2)
    return int(result)

#1辺の長さ
L = getDistance(x1, y1, x2, y2)

