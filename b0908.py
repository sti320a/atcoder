N = int(input())

words = []
for i in range(0,N):
    word = input()
    words.append(word)

# 同じ単語があるかチェック

appeared = []
for word in words:
    if word in appeared:
        print("No")
        exit()
    else: 
        appeared.append(word)

# つながりができているかチェック
endChar = words[0][0]
for word in words:
    if word[0] != endChar:
        print("No")
        exit()
    else:
        endChar = word[-1]

print("Yes")