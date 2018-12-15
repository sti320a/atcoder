S = input()
cnt = 0

def reverse(S, cnt):

    if len(S) <= 0:
        print(str(cnt))
        return 

    for i in range(0, len(S)):
        if i + 1 >= len(S):
            break
        if S[i] == "B" and S[i+1] == "W":
            S = S[0:i] + "W" + "B" + S[i+2:len(S)]
            if S[0] == "W":
                S = S[1:len(S)]
            if S[len(S)-1] == "B":
                S = S[0:len(S)-1]
            cnt += 1
    
    reverse(S, cnt)
    return

reverse(S, cnt)

# print('ans:'+str(ans))
# print(reverse(S, cnt))
