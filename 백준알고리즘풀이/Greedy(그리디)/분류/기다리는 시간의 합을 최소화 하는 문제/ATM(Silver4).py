# 10:29~10:32 /10:32~10:35

# n : 사람 수
# Pi : i번 사람이 돈을 인출하는데 걸리는 시간
# answer : 모든 사람이 돈을 인출하는데 필요한 시간의 합의 최소값
# ======================================================
import sys

input = sys.stdin.readline

# n 입력
n = int(input())
# 인출 시간 입력
times = list(map(int, input().split()))
# 인출 시간 정렬
times.sort()

# answer 변수
answer = 0
# n만큼 반복하면서
for i in range(n):
    # answer += 현재숫자 * (전체 합에서 몇번 해당숫자가 나오는 횟수)
    answer += times[i] * (n - i)

# answer 출력
print(answer)