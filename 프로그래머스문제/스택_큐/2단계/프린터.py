from collections import deque

def solution(priorities, location):
    answer = 0
    priorities = deque(priorities)
    length = len(priorities)
    
    while priorities:
    
        doc = priorities.popleft()
        answer += 1
        location -= 1
        for priority in priorities:
            if doc < priority: 
                priorities.append(doc)

                if location < 0:
                    location = length-1
                answer-=1
                break

        if location == 0:
            answer+=1
            break
        
            
    return answer
