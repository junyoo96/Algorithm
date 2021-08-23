#dfs method
def solution(numbers, target):
    answer = 0
    n = len(numbers)
    
    def dfs(idx,result):
        if idx == n: # if index is last index
            if result == target: # result matches to target number 
                nonlocal answer # variable answer binds to variable answer(one level outside of function)
                answer += 1
            return 
        else:
            dfs(idx+1,result+numbers[idx]) # sum 
            dfs(idx+1,result-numbers[idx]) # minus
    dfs(0,0)
        
    return answer
  
#bfs method
from collections import deque
def solution(numbers, target):
    answer = 0
    queue = deque() # convert into deque
    n = len(numbers) 
    
    queue.append([numbers[0],0]) # sum
    queue.append([-1*numbers[0],0]) # minus

    while queue: 
        num,idx = queue.popleft() # pop first one from deque
        idx += 1
        if idx < n:
            queue.append([num+numbers[idx],idx]) # sum 
            queue.append([num-numbers[idx],idx]) # minus
        else: # if index is last number
            if num == target: # if result matches to target number
                answer += 1
            
    return answer
