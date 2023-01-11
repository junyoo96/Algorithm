# 10:48~10:59 / 11:04~11:17

# n : 도시 수(2~100,000)
# 도시
    # 일직선 도로 위에 있음
    # 1km마다 1리터 기름 사용
# answer : 표준 출력으로 제일 왼쪽 도시에서 제일 오른쪽 도시로 가는 최소 비용 출력
#============================================
import sys
input = sys.stdin.readline

# n 입력
n = int(input())
# 도로 길이 입력
roads = list(map(int, input().split()))
# 주유소의 리터당 가격
prices = list(map(int, input().split()))

# 이전 주유 가격 = 첫번재 도시 주유 가격
prev = prices[0]
answer = 0
# n-2만큼 반복하면서
for i in range(n - 1):
    # 만약 현재 도시 주유 가격이 이전주유 가격보다 작다면
    if prices[i] < prev:
        # 주유 가격 갱신
        prev = prices[i]
    # anwser += 현재 주유 가격 * 현재 도로 길이
    answer += prev * roads[i]

# answer 출력
print(answer)