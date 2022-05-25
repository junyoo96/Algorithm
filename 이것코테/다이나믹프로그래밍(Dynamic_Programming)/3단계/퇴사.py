n = int(input()) # 전체 상담 개수
t = [] # 각 상담을 완료하는데 걸리는 기간
p = [] # 각 상담을 완료했을 때 받을 수 있는 금액
dp = [0] * (n + 1) # 다이나믹 프로그래밍을 위한 1차원 dp 테이블 초기화
answer = 0 # 현재 날짜까지의 날짜 중 가장 큰 수익을 출력

# 각 상담을 완료하는데 걸리는 기간과 받을 수 있는 금액을 입력받기
for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

# 리스트를 뒤에서부터 거꾸로 확인
for i in range(n - 1, -1, -1):
    #현재 상담이 퇴사일전에 끝나는지 확인
    time = t[i] + i
    # 상담이 퇴사일 전에 끝나는 경우
    if time <= n:
        # 기존 최대 이윤과 (현재 상담일자의 이익(p[i]) + 현재 상담을 마친 일자부터의 최대 이익(dp[t[i] + i]) 비교
        # dp[i] : i번째 날부터 마지막 날까지 낼 수 있는 최대 이익
        dp[i] = max(p[i] + dp[time], answer)
        answer = dp[i]
    # 상담이 퇴사일 전에 끝나지 않는 다면
    else:
        # 해당 날 이후의 최대 이익이 해당 일부터의 최대 이익이 됨
        dp[i] = answer

print(answer)