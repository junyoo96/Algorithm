from collections import deque
import copy

# v : 노드 개수
v = int(input())
# indegree : 노드에 대한 진입차수
indegree = [0] * (v + 1)
# graph : 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프)
graph = [[] for i in range(v + 1)]
# time : 각 강의 시간을 0으로 초기화
time = [0] * (v + 1)

# 방향 그래프의 모든 간선 정보 입력받기
for i in range(1, v + 1):
    # data : (강의 시간, 선수과목1, 선수과목2, ...)
    data = list(map(int, input().split()))
    time[i] = data[0] # 강의 시간 저장
    for x in data[1:-1]: # 선수과목에 대해
        indegree[i] += 1 # 현재 과목 i에 대한 진입 차수 증가
        graph[x].append(i) # 선수과목 x를 듣고 들을 수 있는 과목 i를 저장(선수과목에서 현재 과목으로 가는 간선 정보 표시)

# 위상 정렬 함수
def topology_sort():
    # result : 각 강의를 수강하기 위해 걸리는 최소 시간
    # time을 deep copy 하는 이유는
        # time에 각 강의만 수강하는데 걸리는 시간을 가져오기 위해서
        # 단순 대입 연산을 하면 값이 변경될 때 문제가 발생할 수 있기 때문에
    result = copy.deepcopy(time)
    q = deque()

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때가지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            # now : 현재 과목
            # i : 현재 과목을 들은 경우 들을 수 있는 과목
            # max를 하는 이유는 과목 i의 수강 시간에 선수과목 now의 시간을 더해 더 오래 시간이 걸리는 경우의 시간 값을 저장하는 방식으로 result 테이블을 갱신하기 위해
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
    # 위상 정렬을 수행한 결과 출력
    for i in range(1, v + 1):
        print(result[i])

topology_sort()



