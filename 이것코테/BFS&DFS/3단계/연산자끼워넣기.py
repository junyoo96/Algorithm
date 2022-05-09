# 정식 답안(DFS 방식) - 256ms
n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split()) # 더하기, 빼기, 곱하기, 나누기 연산자 개수 입력받기
min_value = 1e9 # 최솟값 초기화
max_value = -1e9 # 최대값 초기화

# 연산자 조합을 DFS 방식으로 구현
    # i : 현재 몇번째 진행했는지
    # now : 현재 값
def dfs(i, now):
    global min_value, max_value, add, sub, mul, div

    # 모든 연산자를 다 사용한 경우, 최솟값과 최대값 업데이트
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        # 각 연산자에 대해 재귀적으로 수행
        if add > 0:
            # 연산자 사용했으니 남은 횟수 빼기
            add -= 1
            dfs(i + 1, now + data[i])
            # add로 시작하는 dfs 모두 수행했으니 다른 연산자로 먼저 시작하는 하기 전에 add 더해서 이전 횟수로 복구하기
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            # 나눌 때 나머지 제거
            dfs(i + 1, int(now / data[i]))
            div += 1

# DFS 메서드 호출
dfs(1, data[0])

print(max_value)
print(min_value)

#=================================================================
# 내가 풀은 방식(중복 순열 방식) - 1204ms
# 10:09~10:17
# 10:43~11:34

# n-1: 연산자 개수
# 주어진 수의 순서 바꾸면 안됨
# 연산자 우선 순위 무시하고 앞에서 진행
# 나눗셈은 몫만 취함
# 음수를 양수로 나눌 때 : 양수로 바꾸고 목을 취한뒤 음수로 변환
from itertools import permutations

n = int(input()) #숫자 개수 # 주의
numbers = list(map(int, input().split()))

operators = [] # 연산자 저장
tmp = list(map(int, input().split()))

# 연산자 기호형태로 변경
for i in range(4):
    for _ in range(tmp[i]):
        # 덧셈인 경우
        if i == 0:
            operators.append('+')
        # 뺄셈인 경우
        elif i == 1:
            operators.append('-')
        # 곱셈인 경우
        elif i == 2:
            operators.append('*')
        # 나눗셈인 경우
        elif i == 3:
            operators.append('/')

# 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하기
result_min = 1e9 # 10억 # 주의 - 10억 표시
result_max = -1e9 # -10억

# 경우의 수 순열(순서 상관있음)
operators_p = permutations(operators, len(operators))

# 조합한 것 계산
# 연산자 조합 반복하면서
for operator in operators_p:
    val = numbers[0]
    # 숫자 반복하면서
    for i in range(n-1):
        if operator[i] == '+':
            val += numbers[i + 1]
        elif operator[i] == '-':
            val -= numbers[i + 1]
        elif operator[i] == '*':
            val *= numbers[i + 1]
        elif operator[i] == '/':
            if (val < 0 and numbers[i + 1] >= 0): # 주의 - 문제에서 나온 순서대로 그대로 구현하기
                m = abs(val) // numbers[i+1]
                val = m * -1
            else:
                val = val // numbers[i + 1]

    # 만약 계산한 값이 max이면
    result_max = max(result_max, val)
    # 만약 계산한 값이 min이면
    result_min = min(result_min, val)

print(result_max)
print(result_min)


