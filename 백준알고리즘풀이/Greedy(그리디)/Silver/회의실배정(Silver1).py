# 9:43~9:52 / 10:00~

# n : 회의 수
    # 시작시간, 끝나는 시간
    # 두 시간이 동일할 수 있음
# answer : 회의가 겹치지 않으면서 회의실을 사용할 수 있는 최대 개수
# 최적해 방안 : 회의를 제일 많이 열기 위해서는 빨리 끝나는 순서대로 회의실을 사용하면 됨
#===============================================================
import sys

answer = 0
# n 입력
n = int(sys.stdin.readline()) # 주의 - input()말고 readline() 사용해야 훨씬 빨리 처리됨
# 회의 시작시간, 끝 시간 입력
meetings = []
for _ in range(n):
    meetings.append(tuple(map(int, sys.stdin.readline().split()))) # 주의 - 입력받은 것 tuple형태로 바로 변경

# 회의 시간 리스트를 끝나는 시간 기준으로 정렬
# 주의 - 회의가 끝나는 시간이 동일한 경우, 시작시간이 빠른 회의를 먼저 해야하므로 끝나는 시간이 동일한 회의들안에서 다시 시간 기준으로 오름차순 정렬해야함
meetings.sort(key=lambda x: (x[1], x[0])) # 주의 - lambda 사용해 다른 기준으로 정렬 여러번 하기

previous_end = 0
# 희의 시간 리스트를 반복하면서
for start, end in meetings:
    # 만약 현재회의의 시작 시간이 이전회의의 끝 시간이보다 크거나 같다면
    if start >= previous_end:
        # answer 증가
        answer += 1
        # 끝나는 시간을 현재회의의 끝나는 시간으로 갱신
        previous_end = end

# answer 출력
print(answer)