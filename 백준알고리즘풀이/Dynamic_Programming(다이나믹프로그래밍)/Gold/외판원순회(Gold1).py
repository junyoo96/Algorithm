# 9:44~ / 아이디어 생각 못함
# 참고 : https://velog.io/@kimdukbae/BOJ-2098-%EC%99%B8%ED%8C%90%EC%9B%90-%EC%88%9C%ED%9A%8C-Python

# n : 도시 개수
    # 도시들 사이에 길(없을 수도 있음)
    # 어느 한도시에서 출발해 n개 도시 모두 거치고 다시 원래 도시로 돌아오는 순회하려고 함
        # 한번 갔던 도시는 다시 갈수 없음(맨 마지막에 출발했던 도시로 돌아오는 건 예외)
        # 가장 적은 비용으로 여행하려고 함
# 도시 i에서 도시 j로 가기 위한 비용
    # 비용은 대칭적이지 않음
    # 비용은 양의 정수
    # 도시에서 도시로 갈 수 없는 경우는 비용이 0으로 표시됨
# answer : 외판원의 순회에 필요한 최소 비용 출력
#====================================================================================
# 방법 1 - DP 적용 방식
    # 완전탐색 방식이 시간초과되는 문제를 DP를 적용해 해결한 방식
import sys

input = sys.stdin.readline
n = int(input())
dists = [list(map(int, input().split())) for _ in range(n)]
# n개의 비트를 모두 켜기(on)
    # 1 : 방문했음
    # 0 : 방문안함
VISITED_ALL = (1 << n) - 1

# DP를 위한 캐시 초기화
# 도시의 개수(N)에 대응하고 (1 << N)을 통해 방문한 도시 집합(visited)에 대응
# cache[N][visited] : N번 -> visited에서 방문 X한 도시 -> 0번 도시(시작도시) 경로 저장한다고 생각하기
cache = [[None] * (1 << n) for _ in range(n)]
INF = float('inf') # 무한을 나타내기 위한 변수

def find_path(last, visited):
    # visited : 도시 방문 여부 집합(비트로 표현, 비트로 표현한 이유는 리스트로 표현했을 때보다 빠르기 때문)
        # 예시
        # n(도시의 수)가 8일 때, 11110000으로 표현하면
        # 0,1,2,3번 도시는 방문하지 않았고, 4,5,6,7번 도시는 방문했다는 것을 표현함
        # 여기서 방문한 중간경로의 구체적인 순서는 중요하지 않음
    if visited == VISITED_ALL:
        # 마지막 방문 도시 출발 - 0번째(출발 도시) 사이에 경로가 존재하면, 경로 값을 반환
            # or 연산자
                # 연산자를 통해 마지막 방문 도시와 0번째(시작도시) 사이의 경로가 존재하면 경로값을 반환하고
                # 길이 없다면 무한값을 반환해서 답이 될 수 없게 함
        return dists[last][0] or INF # 마지막 도착 도시에서 출발 도시인 0으로 가야됨(문제 조건)

    # DP 사용
    # cache값이 None이 아니라는 것은 last와 visited 계산이 이미 수행됐고, 중복호출 되었다는 뜻 -> 다시 계산하지 않고 값만 바로 반환하도록해서 중복계산을 없애 효율성 높음
    if cache[last][visited] is not None:
        return cache[last][visited]

    # 방문하지 않은 모든 도시를 모두 방문해서 그중 비용의 최소값을 선택해야함
    tmp = INF
    for city in range(n):
        # 만약 해당 도시를 아직 방문하지 않았고, 해당 도시까지의 길이 존재한다면
            # visited & (1 << city) == 0 : 만약 해당 도시를 아직 방문하지 않았다면
            #  cities[last][city] != 0 : 길이 없지 않다면(길이 없는 경우는 0으로 표시하므로)
        if visited & (1 << city) == 0 and dists[last][city] != 0:
            tmp = min(tmp, find_path(city, visited | (1 << city)) + dists[last][city])
    # 모든 도시를 방문하고 최소로 경신된 tmp를 cache에 저장
    cache[last][visited] = tmp
    return tmp

# 점화식 시작
    # start : 0번 인덱스의 도시를 시작 도시로 지정
        # 시작도시는 어디가 되어도 결국 정답 경로를 찾게되기 때문
    # visited : 방문 도시 비트로 표현
answer = find_path(0, 1 << 0)
print(answer)

#====================================================================================
# 방법 2 - 완전탐색으로 풀기
    # 시간복잡도 : O(N!) - N이 커지면 시간초과
def tsp(D):
    N = len(D)
    inf = float('inf')
    ans = inf
    # 모든 도시를 방문했다는 것을 나타내는 비트 생성
        # n개의 비트를 모두 1로 켜기(on)
        # 1 : 방문했음
        # 0 : 방문안함
    VISITED_ALL = (1 << N) - 1

    # 각 도시를 방문하는 재귀함수
    def find_path(start, last, visited, tmp_dist):
        # start : 순회 시작노드
        # last : 현재까지 방문한 중간 경로의 마지막 방문 도시
        # visited : 도시 방문 여부 집합(2진수로 표현)
            # 예시
                # n(도시의 수)가 8일 때, 11110000으로 표현하면
                # 0,1,2,3번 도시는 방문하지 않았고, 4,5,6,7번 도시는 방문했다는 것을 표현함
        # tmp_dist : 중간경로까지의(지금까지 순회 비용)

        nonlocal ans
        # 만약 모든 도시를 방문했다면
        if visited == VISITED_ALL:
            # 마지막 방문 도시에서 시작 도시까지의 비용 계산
            return_home_dist = D[last][start] or inf
            # 최소값 비교해서 최소값 갱신
            ans = min(ans, tmp_dist + return_home_dist)
            # 종료
            return

        # 모든 도시를 방문하지 않은 경우, 방문하지 않은 각 도시 방문
        for city in range(N):
            # 만약 해당 도시를 아직 방문하지 않았고, 해당 도시까지의 길이 존재한다면
                # visited & (1 << city) == 0 : 만약 해당 도시를 아직 방문하지 않았다면
                # D[last][city] != 0 : 길이 없지 않다면(길이 없는 경우는 0으로 표시하므로)
            if visited & (1 << city) == 0 and D[last][city] != 0:
                # 해당 도시까지의 길 방문
                    # visited | (1 << city) : 해당 도시 방문처리
                    # tmp_dist + D[last][city] : 시작 도시부터 해당 도시까지의 비용
                find_path(start, city, visited | (1 << city), tmp_dist + D[last][city])

        # 무에서 각 도시를 처음으로 방문하면 해나감
        # 모든 도시가 시작점이 될 수 있으므로 다 테스트
        for c in range(N):
            # 1 << c : 방문 도시를 표현
            # tmp_dist(중간경로까지의 비용)를 0으로 시작
            find_path(c, c, 1 << c, 0)

        return ans