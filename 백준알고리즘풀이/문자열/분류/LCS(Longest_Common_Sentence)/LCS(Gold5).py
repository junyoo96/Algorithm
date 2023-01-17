# 11:46~12:20 / 12:20~ - 아이디어는 맞았으나 구현에서 빠진 로직이 있어서 틀림
# 10:34~10:45/ 10:50~11:10 - 2차원 DP 방식으로 맞춤
#=============================================================
# 최적화 코드
# Dynamic Programming(2차원 배열 방식)
# 시간 : 576ms

# 열 문자열
str1 = input()
# 행 문자열
str2 = input()
str1_length = len(str1)
str2_length = len(str2)

# 2차원 배열 캐시(값을 누적하면서 부분수열이 길이를 저장)
arr = [[0] * (str1_length + 1) for _ in range(str2_length + 1)]
for i in range(1, str2_length + 1):
    for j in range(1, str1_length + 1):
        # 현재 위치의 문자열이 동일하다면
        if str2[i - 1] == str1[j - 1]:
            arr[i][j] = arr[i - 1][j - 1] + 1
        # 동일하지 않다면
        else:
            # 현재 위치의 값 갱신 = max(상,좌) + 현재 위치의 값
            arr[i][j] += max(arr[i - 1][j], arr[i][j - 1])

# 캐시의 마지막 행열 부분이 부분 수열 중 가장 긴 수열의 길이가 됨
print(arr[-1][-1])

#=============================================================
# Dynamic Programming(1차원 배열 방식)
# 시간 : 236ms

# 한 자씩 비교할 문자열
str1 = input()
# 기준 문자열
str2 = input()
str1_length = len(str1)
str2_length = len(str2)

# 1차원 배열 캐시(기존 2차원 배열보다 순회 시간 줄일 수 있음)
arr = [0] * str2_length
# 한 자씩 비교할 문자열을 반복하면서
for i in range(str1_length):
    cnt = 0
    # 기준 문자열과 비교하면서
    for j in range(str2_length):
        # 만약 글자가 다른 경우 누적 변수의 값이 해당 위치의 값보다 작은 경우 해당 값으로 교체(누적값에서는 이전위치까지의 최대값이 계속해서 저장됨)
        if cnt < arr[j]:
            cnt = arr[j]
        # 현재 위치의 문자열이 동일하다면
        elif str1[i] == str2[j]:
            # 누적한 값에서 1을 더해서 갱신
            arr[j] = cnt + 1

# 캐시의 마지막 행열 부분이 부분 수열 중 가장 긴 수열의 길이가 됨
print(max(arr))