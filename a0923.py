A, B, C = map(int, input().split())

ABC = [A,B,C]
ABC = sorted(ABC, reverse=True)

print(int(str(ABC[0]) + str(ABC[1])) + ABC[2]) 
    


