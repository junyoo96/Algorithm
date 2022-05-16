#10:07~10:37

#answer code(가장 간단한 방법, 그러나 M의 크기가 커질경우 시간 초과 판정)
# n: 숫자 배열 크기
# m: 총 더할 횟수
# k: 연속해서 같은 숫자 더할 수 있는 횟수
n, m, k = map(int, input.split())
# data : 더할수 있는 수 종류
data = list(map(int,input.split()))

data.sort() # 수 배열 오름차순 정렬
first = data[n-1] # 첫번째 큰 수
second = data[n-2] # 두번째 큰 수

result = 0
while True:
    # 1. 첫번째 큰 수 더하는 부분
    for i in range(k): # 가장 큰 수 k번 더하기
        if m == 0: # 총 더할 횟수 넘으면 탈출
            break
        result += first # 첫번째 큰 수 더하기
        m -= 1 # 총 더할 횟수 감소
    # 2. 두번째 큰 수 더하는 부분
    if m == 0: # 총 더할 횟수 넘으면 탈출
        break
    result += second # 두번째 큰 수 더하기
    m -= 1 # 총 더할 횟수 감소

print(result)
#==========================================================================================

#answer code(수학적 아아디어를 사용한 방법, 시간 초과 판정 해결 코드)
n, m, k = map(int, input.split())
data = list(map(int,input.split()))

data.sort()
first = data[n-1] # 첫번째 큰 수
second = data[n-2] # 두번째 큰 수

#첫번째로 큰 수 더해지는 횟수 계산
count = int(m / (k+1)) * k
count += m % (k+1)

#더하기
result = first * count # 첫번째 큰 수 더하기
result += second * (m-count) # 두번째 큰 수 더하기

print(result)
#==========================================================================================

#my code
# 주어진 수 배열 내림 차순으로 정렬

# for M번 동안
    # K번 반복해서 더해졌는지 체크
    # result에 현재 숫자 더하기

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)

check = k
idx = 0

result = 0
for i in range(m):
    if check == 0:
        idx += 1
        check = k
    else:
        idx = 0
        check -= 1
    result += data[idx]

print(result)