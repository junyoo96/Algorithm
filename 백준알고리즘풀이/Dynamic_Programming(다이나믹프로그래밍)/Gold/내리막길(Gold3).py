# 9:54~10:06/10:06~ - DP 아이디어 생각못함

# 지도
    # 칸 : 지점 높이
    # 상하좌우 이동 가능
    # 왼쪽 위칸에서 오른쪽 아래 칸으로 이동
    # 항상 높이가 더 낮은 지점으로 이동
# answer : 항상 내리막길로만 이동하는 경로들 개수
# DFS + DP 혼합 문제
    # DFS로만 풀면 시간 초과나므로, 이미 갔던 길에 대해서는 DP 사용해야함
# 점화식
    # 현재 위치부터 목표지점까지 갈 수 있는 경우의 수 = 상하좌우 방향 중 갈 수 있는 방향의 위치부터 목표지점까지 갈 수 있는 경우의 수의 합

import sys
sys.setrecursionlimit(100000) # 주의
input = sys.stdin.readline

# answer
answer = 0
# m, n 입력
m, n = map(int, input().split())
# 지도 입력
array = [list(map(int, input().split())) for _ in range(m)]

# dp 테이블 생성
dp = [[-1] * n for _ in range(m)]
# 방향 리스트 생성
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# dfs 함수(출발 좌표)
def dfs(x, y):
    # 만약 목표 지점에 도착했다면
    if x == m - 1 and y == n - 1:
        return 1

    # 중요 - 이미 방문한적 있다면 그 위치에서 출발하는 경우의 수 리턴
    if dp[x][y] != -1:
        return dp[x][y]

    # 상하좌우 방향 중 갈 수 있는 방향의 위치부터 목표지점까지 갈 수 있는 경우의 수의 합 구하기
    ways = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 만약 올바른 범위가 맞다면
        if 0 <= nx < m and 0 <= ny < n:
            # 만약 현재 좌표보다 이동할 좌표가 내리막길이라면
            if array[nx][ny] < array[x][y]:
                # 현재 위치에서 갈 수 있는 경우의 수 더하기
                ways += dfs(nx, ny)

    # 현재 위치에서 목표 지점까지 갈 수 있는 경우의 수 = 현재 위치를 기준으로 상하좌우 방향의 위치부터 목표지점까지 갈 수 있는 경우의 수의 합
    dp[x][y] = ways
    return dp[x][y]

# DFS이기 때문에 목표지점부터 거꾸로 계산되어서 최종적으로 출발지점에 출발지점부터 목표지점까지의 경우의 수가 저장되어있음
answer = dfs(0, 0)
# answer 출력
print(answer)