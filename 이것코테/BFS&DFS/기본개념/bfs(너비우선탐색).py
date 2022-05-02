from collections import deque 

#BFS 메서드 정의 
def bfs(graph, v, visited):
	queue = deque([v]) # deque 라이브러리 사용 
	visited[v] = True # 현재 노드 방문 처리 
	
	while queue:
		#큐에서 하나의 원소를 뽑아 출력 
		v = queue.popleft() 
		print(v, end= ' ')
		#해당 원소와 연결된, 아직 방문하지 않는 원소들을 큐에 삽입 
		for i in graph[v]:
			if not visited[i]:
				queue.append(i)
				visited[i] = True # 방문 처리 
				
#각 노드가 연결된 정보를 2차원 리스트로 표현 
graph = [ 
	[],
	[2, 3, 8],
	[1, 7],
	[1, 4, 5],
	[3, 5],
	[3, 4],
	[7], 
	[2, 6, 8],
	[1, 7]
]
#각 노드가 방문된 정보 
visited = [False] * 9 

#정의된 BFS 함수 호출(vertex 1부터 시작)
bfs(graph, 1, visited)
