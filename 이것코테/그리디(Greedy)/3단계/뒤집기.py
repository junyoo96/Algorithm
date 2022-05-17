# 11:18~

# 연속된 부분으로 그룹을 분리해서 0으로 이루어진 그룹과 1로 이루어진 그룹 수 중 더 작은 그룹수가 최소 횟수가 됨

answer = 0
data = input()

group_zero = 0 # 0인 그룹 수
group_one = 0 # 1인 그룹 수

# 첫 번째 원소에 대해서 처리
if data[0] == '0':
    group_zero += 1
else:
    group_one += 1

# 주의 - 앞에 숫자와 뒤에 숫자 비교하는 코드 암기하기
# 현재 숫자와 다음 숫자 비교할 때는 전체길이의 -1큼 반복
for i in range(len(data) - 1): # 주의 - n이 문자열인지 숫자인지 확인하기
    if data[i] != data[i + 1]:
        # 다음 수에서 0으로 바뀌는 경우
        if data[i + 1] == '0':
            group_zero += 1
        # 다음 수에서 1로 바뀌는 경우
        else:
            group_one += 1

answer = min(group_zero, group_one)

print(answer)
