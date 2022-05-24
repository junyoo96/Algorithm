#10:03~

# n,m : 금광 크기
    # 가장 왼쪽 위 (1,1)
# 각 칸에 특정 크기 금 있음
# 첫번째 열부터 금 캐기 시작
    # 맨처음에는 첫번째 열 어느 행에서든 출발
    # m번에 걸쳐서 오른쪽위, 오른쪽, 오른쪽 아래 3가지 중 하나 위치로 이동

# answer : m번에 걸쳐서 움직였을 때 채굴자가 얻을 수 있는 금의 최대 크기(m열에서 금의 최대 크기 출력)
answer = 0

t = int(input())

# 움직이기 위한 방향 리스트
dx = [-1, 0, 1]
dy = [-1, -1, -1]

# 테스트 케이스 입력
for _ in range(t):
    n, m = map(int, input().split())  # 금광 정보 입력
    array = list(map(int, input().split()))

    # 다이나믹 프로그래밍 위해 2차원 DP 테이블 초기화
    dp = []
    idx = 0
    for i in range(n):
        dp.append(array[idx:idx + m]) # 주의 - 1차원으로 입력받은 것 2차원으로 행 나눠서 받는 방법 암기하기
        idx += m

    for i in range(1, m): # 열
        for j in range(n): # 행
            candidate = []
            # 3방향(왼쪽 위, 왼쪽, 왼쪽 아래)에서 오는 경우 확인해서 제일 금광이 많은 경우 계산하기
            for a in range(3):
                if (j + dx[a]) < 0 or (j + dx[a]) >= n or (i + dy[a]) < 0 or (i + dy[a]) >= m:
                    continue
                candidate.append(dp[j + dx[a]][i + dy[a]])

            # 금강 많은 경우로 DP 갱신
            dp[j][i] = dp[j][i] + max(candidate)

    # m번에 걸쳐서 움직였을 때 채굴자가 얻을 수 있는 금의 최대 크기(마지막 열인 m열에서 금의 최대 크기 출력)
    for i in range(n):
        answer = max(answer, dp[i][m - 1])

    print(answer)
