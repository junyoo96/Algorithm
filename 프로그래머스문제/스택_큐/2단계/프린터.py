# 2ㅅㅣㄱㅏㄴ ㅊㅗㄱㅗㅏ 

def solution(priorities, location):
    answer = 
    priorities = deque(priorities)
    m = max(priorities)
    while priorities:
        doc = priorities.popleft()
        
        if doc == m:
            answer += 1
            
            if location == 0:
                break 
            else:
                location -= 1
            m = max(priorities)
        else:
            priorities.append(doc)
            
            if location == 0:
                location = len(priorities)-1
            else:
                location -= 1
    
    return answer
