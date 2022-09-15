# 틀림
# 틀림

# 숫자로만 이루어진 문자열 S
# 가장 큰 수 구하기

# 최적해 방안 : 기본적으로 곱하기가 우선이지만, 0이나 1인 숫자가 계산에 들어가는 경우 +가 우선됨

numbers = list(map(int, input())) # 각 자리 숫자 리스트로 변환
result = numbers[0] # 최대 값

for i in range(1, len(numbers)):
    # 더하기 수행하는 경우
    if result <= 1 or numbers[i] <= 1:
        result += numbers[i]
    # 곱하기 수행하는 경우
    else:
        result *= numbers[i]

print(result)