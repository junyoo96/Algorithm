# 9:38~10:00 / 10:00~
# 12:52~1:07/1:07~1:18
# 수빈 N(0~100,000), 동생 K(0~100,000)
# 수빈 : 걷거나, 순간이동 가능
    # 걷기 : 1초후에 X-1이나 X + 1로 이동
    # 순간이동 : 0초후에 2*X로 이동
# answer : 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇초 후인지
#================================================================
from collections import deque

answer = 0 # answer 변수
MAX = 100001 # 장소 크기
n, k = map(int, input().split()) # N, K 입력
visited = [-1] * MAX # 방문 리스트

# queue에 현재 위치 추가
queue = deque()
queue.append(n)
# 중요 - 현재 위치 방문 여부와 해당위치까지 가는데 걸리는 최단시간을 저장
visited[n] = 0

# queue를 반복하면서
while queue:
    # queue에서 현재위치 꺼내기
    pos = queue.popleft()
    # 만약 현재위치가 동생위치와 같다면
    if pos == k:
        # 현재까지 지난 시간 저장
        answer = visited[k]
        break

    # 이동과 순간이동을 반복하면서
    for next_pos in (pos - 1, pos + 1, pos * 2):
        # 이동한 위치가 올바른 범위안이고 아직 방문안했다면
        if 0 <= next_pos < MAX and visited[next_pos] == -1:
            # 순간이동의 경우
            if next_pos == pos * 2:
                # 0초 걸림
                visited[next_pos] = visited[pos]
                # 순간이동의 경우 0초가 걸리므로 일반이동보다 우선하기 위해서 queue의 맨 앞에 추가
                queue.appendleft(next_pos) # 주의 - 순간이동을 우선시 하는 것을 구현하기 위해 PriortyQueue를 사용하면 삭제시 deque보다 시간이 더 오래 걸림으로 appendleft 함수를 사용해서 우선순위를 구현함
            # 일반이동의 경우
            else:
                # 1초 걸림
                visited[next_pos] = visited[pos] + 1
                queue.append(next_pos)

# answer 출력
print(answer)