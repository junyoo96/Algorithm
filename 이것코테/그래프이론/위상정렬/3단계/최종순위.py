#9:23~

# n : 참가팀 수 
# answer 
 # 순위를 알 수 있는 경우, 올해 순위 출력 
 # 알 수 없는 경우, ? 출력
 # 데이터 일관성 없어서 순위 정할 수 없는 경우, IMPOSSIBLE 출력

# tc 입력 
# n : 참가팀수 
# 작년에 팀의 순위 
# m: 상대적인 등수가 바뀐 쌍의 수 
# a,b를 포함하고 있는 m개의 줄(상대적인 등수가 바뀐 2팀)

# 위상정렬 알고리즘으로 풀기 
  # 정해진 우선순위에 맞게 전체 팀들의 순서를 나열해야하기 때문 
  # 팀간의 순위정보를 그래프 정보로 표현한 뒤에 위상정렬 알고리즘을 이용해 해결 
    # 순위정보에 따라 자기보다 낮은 등수를 가진 팀을 가리키도록 방향 그래프 만들기 

from collections import deque

# 테스트 케이스 만큼 반복 
for tc in range(int(input())):
  # 노드의 개수 입력 받기 
  n = int(input())
  # 모든 노드에 대한 진입차수는 0으로 초기화 
  indegree = [0] * (n + 1)
  # 각 노드에 연결된 간선 정보를 담기 위한 인접 행렬 초기화 
  graph = [[False] * (n + 1) for i in range(n + 1)]
  # 작년 순위 정보 입력 
  data = list(map(int, input().split()))

  # 방향 그래프의 간선 정보 초기화 
  for i in range(n):
    for j in range(i + 1, n):
      # 자기보다 낮은 등수를 가진 팀을 가리키도록 표현 
        # i : 높은 등수, j : 낮은 등수 
      graph[data[i]][data[j]] = True
      # 낮은 등수의 진입차수 증가 
      indegree[data[j]] += 1

  # 올해 변경된 순위 정보 입력 
  m = int(input())
  for i in range(m):
    a, b = map(int, input().split())
    # 간선의 방향 뒤집기 
    if graph[a][b]: # a(작년에 높은 등수, 올해에는 낮은 등수), b(작년에 낮은 등수, 올해에는 높은 등수) 
     # 높은 등수가 낮은 등수를 가리키게 표현
      graph[a][b] = False
      graph[b][a] = True
      # 마찬가지로 진입차수도 변경 
      indegree[a] += 1 # 낮은 등수이면 진입차수 증가
      indegree[b] -= 1 # 높은 등수이면 진입차수 감소 
    else: # a(작년에 낮은 등수, 올해에는 높은 등수), b(작년에 높은 등수, 올해에는 낮은 등수)
      graph[a][b] = True
      graph[b][a] = False
      indegree[a] -= 1
      indegree[b] += 1
      
  # 위상 정렬(Topology Sort) 시작   
  result = [] # 알고리즘수행 결과를 담을 리스트
  q = deque() # 큐 기능을 위한 deque 라이브러리 사용 

  # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입 
  for i in range(1, n + 1):
    if indegree[i] == 0:
      q.append(i)

  certain = True # 위상 정렬 결과가 오직 하나인지 여부 
  cycle = False # 그래프 내 사이클이 존재하는지 여부 

  # 정확히 노드의 개수만큼 반복 
  for i in range(n):
    # 큐가 비어있다면 사이클이 발생했다는 의미 
    if len(q) == 0:
      cycle = True
      break
    # 큐의 원소가 2개 이상이라면 가능한 정렬 결과가 여러 개라는 의미
    if len(q) >= 2:
      certain = False
      break
    # 큐에서 원소 꺼내기 
    now = q.popleft()
    result.append(now)
    # 해당 원소와 연결된 노드들의 진입차수에서 1빼기 
    for j in range(1, n + 1):
      if graph[now][j]:
        indegree[j] -= 1
        # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
        if indegree[j] == 0:
          q.append(j)

  # 사이클이 발생하는 경우(일관성이 없는 경우)
  if cycle:
    print("IMPOSSIBLE")
  # 위상 정렬 결과가 여러 개인 경우 
  elif not certain:
    print("?")
  # 위상 정렬을 수행한 결과 출력 
  else:
    for i in result:
      print(i, end=' ')
    print()
