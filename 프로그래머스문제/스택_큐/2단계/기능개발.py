#12:55 ~ 13:50
#실패
def solution(progresses, speeds):
    answer = []
    
    #배포 개수 
    cnt = 0
    #지나간 시간 
    day = 0
    while progresses:
        #현재 작업이 완료 되었다면 
        if (progresses[0]+day*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)        
            cnt+=1
        #현재 작업이 완료 되지않았다면 
        else:
            #카운트된 완료된 작업들 저장 
            if cnt>0:
                answer.append(cnt)
                cnt=0
            #시간(일) 지나는것 
            day+=1
    #마지막으로 완료된 작업 저장 
    answer.append(cnt)
    return answer
