#11:52 ~ 12:02

# for문- 행 별로 돌면서 가장 숫자가 낮은 카드 선택
# 선택한 행에서 가장 낮은 숫자 카드의 숫자 출력

# n : 행
# m : 열
n, m = map(int, input.split())

# '가장 작은 수'들 중에서 가장 큰 수
result = 0
for i in range(n):
    card = list(map(int, input.split()))
    #현재 행에서 '가장 작은 수' 찾기
    min_val = min(card)
    #'가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_val)

print(result)
