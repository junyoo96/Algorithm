#9:17~
n = int(input())

# 못생긴 수를 담기 위한 테이블(1차원 DP 테이블)
ugly = [0] * n
ugly[0] = 1 # 첫번째 못생긴 수는 1
# 2배, 3배, 5배를 위한 인덱스
i2 = i3 = i5 = 0
# 처음에 곱셈값을 초기화
# 계산한 곱셈값을 저장하는 변수
next2, next3, next5 = 2, 3, 5

# 1부터 n까지의 못생긴 수를 찾기
for l in range(1, n):
    # 곱셈 계산한 결과 중에서 가장 작은 수 선택
    ugly[l] = min(next2, next3, next5)
    # 인덱스에 따라서 곱셈 결과를 증가
    if ugly[l] == next2:
        i2 += 1
        next2 = ugly[i2] * 2
    if ugly[l] == next3:
        i3 += 1
        next3 = ugly[i3] * 3
    if ugly[l] == next5:
        i5 += 1
        next5 = ugly[i5] * 5

# n번째 못생긴 수를 출력
print(ugly[n - 1])


