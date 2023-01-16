# 10:04~

a, b = input().split() # 주의 - 문자열 공백으로 구분받아서 받는 방법
a = int("".join(a[::-1])) # 주의 - 문자열 거꾸로 하는 방법
b = int("".join(b[::-1]))

print(a) if a > b else print(b)