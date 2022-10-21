# 9:21~9:45/9:55~ - 문제 완벽히 이해 못함

# 맵
    # n : 행
    # m : 열
    # 각각의 칸은 육지 또는 바다
# 캐릭터는 북동남서(0,1,2,3)중 한고 바라봄
    # 상하좌우로 이동 가능
    # 바다 공간에는 가지 못함
    # 메뉴얼
        # 1. 현재 위치에서 현재 방향 기준으로 왼쪽 방향부터 차례대로 갈곳 정함
        # 캐릭터의 왼쪽 방향에 아직 가보지 못한 칸이 존재하면, 왼쪽 방향으로 회전후 왼쪽으로 한칸 전진
        # 왼쪽 방향에 가보지 않은 칸이 없다면 왼쪽 방향으로 회전만 수행하고 1단계로 돌아감
        # 만약 네 방향 모두 갔거나 바다인 경우, 바라보는 방향 유지하고 한칸 뒤로가고 1단계로 돌아감
            # 뒤쪽 방향이 바다인 경우 움직임 멈춤
# answer : 이동을 멈출때까지 이동한 칸 수
#=================================================================================
import sys
input = sys.stdin.readline

# n 입력, m 입력
n, m = map(int, input().split())
# x, y, 방향 입력
x, y, direction = map(int, input().split())
# 맵 입력
data = [list(map(int, input().split())) for _ in range(n)]
# 방문 리스트
dp = [[0] * m for _ in range(n)]
dp[x][y] = 1
# 방향 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# answer 변수
answer = 1 # 주의 - 처음 칸도 방문한 칸에 포함
# 이동했는지 여부 변수(false)
turn_time = 0
# 무한으로 반복하면서 - while
while True:
    direction -= 1
    if direction == -1:
        direction = 3

    nx = x + dx[direction]
    ny = y + dy[direction]
    # 만약 왼쪽 방향의 칸이 아직 가보지 못한 칸이고 육지라면
    if dp[nx][ny] == 0 and data[nx][ny] == 0:
        # 캐리터 좌표 왼쪽으로 한칸 이동
        x = nx
        y = ny
        # 해당 칸 방문 처리
        dp[nx][ny] = 1
        # answer 증가
        answer += 1
        # 이동여부 변수 true로 갱신
        turn_time = 0
        # break
        continue
        # 이외의 경우
    else:
        turn_time += 1

    # 4방향 모두 이미 갔거나 바다라면(이동했는지 변수가 false라면)
    if turn_time == 4:
        nx = x - dx[direction] # 주의 - 마이너스 연산 사용해서 뒷방향 계산하기
        ny = y - dy[direction]

        # 만약 뒤쪽 방향 칸이 바다라면
        if data[nx][ny] == 1:
            break
        # 한칸 뒤로 이동
        x = nx
        y = ny
        turn_time = 0

# answer 출력
print(answer)