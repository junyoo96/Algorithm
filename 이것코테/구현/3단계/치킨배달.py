# 10:29~ 10:41/10:47~
# 10:18~10:45 / 10:45~11:12 (54분)

# n : 도시 크기
# 행열은 1,1 부터 시작
# 치킨거리
    # 집과 가장 가까운 치킨집 사이의 거리
    # 도시의 치킨거리 : 모든 집의 치킨 거리의 합
# 치킨 폐업하려고함
# 0 빈칸, 1 집, 2 치킨집
# answer : 도시의 치킨거리가 가장 작게되도록 도시에 있는 치킨집 중에서 최대 M개 고르기

#폐업할 치킨집 조합을 중복없이 뽑기 위해 사용
import itertools

n, m = map(int, input().split())
houses = [] # 집 위치 리스트
chickens = [] # 치킨집 위치 리스트

# 도시를 반복하면서 치킨집과 집 각각 찾아서 리스트에 넣기
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        # 만약 집이라면
        if data[j] == 1:
            houses.append((i, j))
        # 만약 치킨집이라면
        elif data[j] == 2:
            chickens.append((i, j))

# 폐업안할 치킨집 후보 고르기(조합 사용 - 순서상관없이)
chickens_candidates = list(itertools.combinations(chickens, m))

# 폐업안할 치킨집 후보의 모든 경우 수를 계산해서 도시 내 치킨 거리 합의 최솟값 구하기
# 주의 - 치킨 거리 최솟값 1e9로 최대값 초기화하기
answer = 1e9
# 폐업안할 치킨집 후보 반복하면서
for candidate in chickens_candidates:
    # 도시 내 각 집의 치킨 치킨 거리 합
    chicken_distance_sum = 0
    # 각 집을 반복하면서
    for hx, hy in houses:
        chicken_distance = 1e9
        # 각 치킨집을 반복하면서
        for cx, cy in candidate:
            # 치킨 거리 계산
            chicken_distance = min(chicken_distance, abs(hx - cx) + abs(hy - cy))
        chicken_distance_sum += chicken_distance
    # 도시 내 각 지브이 치킨 거리 합의 최솟값 계산
    answer = min(answer, chicken_distance_sum)

print(answer)