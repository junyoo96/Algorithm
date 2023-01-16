n = int(input())
for _ in range(n):
    num, string = input().split() # 주의 - map 사용 안해도됨
    for s in string:
        print(s * int(num), end = '')
    print("")
