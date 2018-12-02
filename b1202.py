S = input()


result = []
for i in range(0, len(S)):
    text = S[i:i+3]
    ans = abs(753 - int(text))
    result.append(ans)

print(min(result))