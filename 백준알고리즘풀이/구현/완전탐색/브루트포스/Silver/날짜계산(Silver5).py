# 12:47~12:50 / 12:50~12:56

# 지구 E, 태양 S, 달 M
    # 1년 = 1, 1, 1
    # 1년이 지날때마다 3수는 1씩 증가
    # 범위를 넘어가면 1로 됨
# ansewr : 주어진 ESM이 우리 연도로 몇년인지 구하기
# ============================================
e, s, m = map(int, input().split())
a = 1
b = 1
c = 1
answer = 1

while True:
    if a == e and b == s and c == m:
        break

    a += 1
    b += 1
    c += 1

    if a > 15:
        a = 1
    if b > 28:
        b = 1
    if c > 19:
        c = 1

    answer += 1

print(answer)