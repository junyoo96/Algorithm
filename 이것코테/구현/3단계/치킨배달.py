#10:29~ 10:41
#10:47~ 11:35

#폐업할 치킨집 조합을 중복없이 뽑기 위해 사용
import itertools

answer = 0

# n : 도시 크기
# m : 가장 수익 많이 낼 수 있는 치킨집의 최대 개수
n, m = map(int, input().split())
house_loc = [] # 집 위치 리스트
chicken_loc = [] # 치킨집 위치 리스트

# 도시를 반복하면서 치킨집과 집 각각 찾아서 리스트에 넣어주기
for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        # 집이면
        if data[c] == 1:
            house_loc.append((r, c))
        # 치킨집이면
        elif data[c] == 2:
            chicken_loc.append((r, c))

# 폐업안할 치킨집 후보 고르기(조합 사용 - 순서상관없이)
chosen_chickens = list(itertools.combinations(chicken_loc, m))

# 폐업안할 치킨집 후보의 모든 경우 수를 계산해서 도시 내 치킨 거리 합의 최솟값 구하기
min_chicken_distance_sum = 1e9 # 치킨 거리 최솟값
# 폐업안할 치킨집 후보 반복하면서
for chosen_chicken in chosen_chickens:
    chicken_distance_sum = 0 # 도시 내 각 집의 치킨 치킨 거리 합
    # 각 집을 반복하면서
    for hx, hy in house_loc:
        chicken_distance = 1e9
        # 각 치킨집을 반복하면서
        for cx, cy in chosen_chicken:
            # 치킨 거리 계산
            chicken_distance = min(chicken_distance, abs(hx-cx) + abs(hy-cy))
        chicken_distance_sum += chicken_distance
    # 도시 내 치킨 거리 합의 최솟값 구하기
    min_chicken_distance_sum = min(min_chicken_distance_sum, chicken_distance_sum)

answer = min_chicken_distance_sum

print(min_chicken_distance_sum)