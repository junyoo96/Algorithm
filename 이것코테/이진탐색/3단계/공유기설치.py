# 10:40~

# n : 집 개수
# c : 공유기 개수
n, c = list(map(int, input().split(' ')))

# 전체 집들의 좌표 정보 입력받기
array = []
for _ in range(n):
    array.append(int(input()))
# 이진 탐색 수행 위해 정렬 수행
array.sort()

start = array[1] - array[0] # 가장 작은 인접한 두 공유기 사이 거리
end = array[-1] - array[0] # 가장 큰 인접한 두 공유기 사이 거리
result = 0 # 가장 인접한 두 공유기 사이 거리

# 가장 작은 인접한 두 공유기 사이 거리가 가장 큰 인접한 두 공유기 사이 거리가 작거나 같은 동안
while start <= end:
    mid = (start + end) // 2 # 공유기 설치해야될 때 설치 후 가장 인접한 두 공유기 사이 거리 의미
    value = array[0] # 첫번째 공유기 좌표
    count = 1 # 설치한 공유기 개수

    # 현재의 mid값을 이용해 공유기 설치
    for i in range(1, n): # 앞에서부터 공유기 설치
        # 현재 좌표 위치가 (앞에서 설치한 제일 가까운 공유기 위치 + 인접거리) 보다 크면 인접거리(mid)를 유지하면서 설치가 가능하므로
        if array[i] >= value + mid:
            value = array[i] # 최근에 설치한 공유기 위치 갱신
            count += 1 # 설치한 공유기 개수 증가
    # c개 이상의 공유기를 설치할 수 있는 경우, 거리를 증가
    if count >= c:
        # start를 증가시켜야 첫번째 공유기 좌표로부터 인접거리가 더 멀어지니까(이진 탐색으로 빠르게 탐색하기 위해 start + 1이 아니라 mid + 1)
        start = mid + 1
        # 최적의 인접 거리 저장
        result = mid
    # c개 이상의 공유기를 설치할 수 없는 경우, 거리를 감소
    else:
        # end를 증가시켜야 첫번째 공유기 좌표로부터 인접거리가 더 가까워지니까((이진 탐색으로 빠르게 탐색하기 위해 end - 1이 아니라 mid - 1)
        end = mid - 1

print(result)