# 2 hour 

def solution(priorities, location):
    answer = 0 
    priorities = deque(priorities) # convert array into deque to make add and pop faster
    m = max(priorities)
    while priorities: # while document exists
        doc = priorities.popleft() # O(1)
        
        if doc == m: # if current document has max priority
            answer += 1 
             
            if location == 0: # if current document is up to print 
                break 
            else:
                location -= 1 # move location 
            m = max(priorities) # update max priority
        else: 
            priorities.append(doc) # append current document 
            
            if location == 0: # update location into end of deque
                location = len(priorities)-1
            else:
                location -= 1 # move location forward
    
    return answer
