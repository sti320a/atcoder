import re

text = input()

def countPattern(text):
    regex = 'aa|bb'
    pattern = re.compile(regex)
    obj = pattern.split(text)
    return obj

ans = countPattern(text)
print(ans)
