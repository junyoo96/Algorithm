#dfs
def solution(n, computers):
    answer = 0
    n = len(computers)
    visited = [0 for i in range(n)]
    
    def dfs(i):
        if visited[i] == 1:
            return
        
        visited[i] = 1
        
        for j in range(n):
            if computers[i][j] == 1:
                dfs(j)
            
    for i in range(n):
        if visited[i] == 1:
            continue
        dfs(i)
        answer += 1
            
    return answer
