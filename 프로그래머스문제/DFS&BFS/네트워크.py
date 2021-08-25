#dfs
def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)] # to check visited node
    
    def dfs(i):
        if visited[i] == 1: # if visited
            return
        visited[i] = 1 # mark visited node
        
        for j in range(n): # check connected node 
            if computers[i][j] == 1: # if connected
                dfs(j)
            
    for i in range(n): # traverse all nodes
        if visited[i] == 0: # if not visited
            dfs(i)
            answer += 1 # add network
            
    return answer

#bfs
def solution(n, computers):
    def bfs(node, visited):
        que = [node] # add node to visit
        visited[node] = 1 #check visited node
        
        while que: # until queue is not empty
            v = que.pop(0) # v : current node
            for i in range(n): # check connected nodes
                if computers[v][i] == 1 and visited[i] ==0: 
                    visited[i] = 1
                    que.append(i) # add connected nodes to queue
        return visited
    
    visited = [0 for i in range(n)] # to check visited node
    answer = 0
    for i in range(n): # traverse all nodes
        try:
            visited = bfs(visited.index(0),visited) 
            answer += 1 # add network 
        except:
            break
    return answer
