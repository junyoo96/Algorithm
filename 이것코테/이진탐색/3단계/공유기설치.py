# 10:40~
# 1:32~ - 아이디어 생각 못함
import sys
input = sys.stdin.readline

# n : 집 개수
# c : 공유기 개수
n, c = list(map(int, input().split(' ')))

# 전체 집들의 좌표 정보 입력받기
houses = [int(input()) for _ in range(n)]
# 이진 탐색 수행 위해 정렬 수행
houses.sort()

start = 1 # 가장 작은 인접한 두 공유기 사이 거리
end = houses[-1] - houses[0] # 주의 - 끝범위는 가장 큰 인접한 두 공유기 사이 거리가 되어야함
answer = 0 # 가장 인접한 두 공유기 사이 거리

# 가장 작은 인접한 두 공유기 사이 거리가 가장 큰 인접한 두 공유기 사이 거리가 작거나 같은 동안
while start <= end:
    mid = (start + end) // 2 # 공유기 설치해야될 때 설치 후 가장 인접한 두 공유기 사이 거리 의미
    position = houses[0] # 첫번째 공유기 좌표
    count = 1 # 설치한 공유기 개수

    # 현재의 mid값을 이용해 공유기 설치
    for i in range(1, n): # 앞에서부터 공유기 설치
        # 현재 좌표 위치가 (앞에서 설치한 제일 가까운 공유기 위치 + 인접거리) 보다 크면 인접거리(mid)를 유지하면서 설치가 가능하므로
        if houses[i] >= position + mid:
            position = houses[i] # 최근에 설치한 공유기 위치 갱신
            count += 1 # 설치한 공유기 개수 증가

    # 만약 설치한 공유기 개수가 설치해야되는 공유기 개수보다 많거나 같다면, 공유기 간 거리를 증가해도 됨
    if count >= c:
        # start를 증가시켜야 첫번째 공유기 좌표로부터 인접거리가 더 멀어지니까
        start = mid + 1
        # 최적의 인접 거리 저장
        answer = mid
    # 설치해야하는 개수만큼 설치못하면, 공유기 간의 거리 감소
    else:
        # end를 증가시켜야 첫번째 공유기 좌표로부터 인접거리가 더 가까워지니까
        end = mid - 1

print(answer)