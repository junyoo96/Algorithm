# 6:15 / 7 : 09
# 트럭은 1초에 1칸씩 움직임 
# 

def solution(bridge_length, weight, truck_weights):
    answer = 0 # 걸린 시간 
    onBridge=[0]*bridge_length # 다리 위에 올라와 있는 트럭들, 0은 빈 도로 
    
    while onBridge : # 다리 위에서 트럭이 없어질 때까지 
        answer+=1 # 시간 증가 
        onBridge.pop(0)
        
        if truck_weights: # 대기 트럭이 있다면 
            if sum(onBridge) + truck_weights[0] <= weight : # 대기 트럭이 들어왔을 때 무게를 버틴다면 
                onBridge.append(truck_weights.pop(0)) # 다리에 트럭 추가 
            else : #다리에 트럭이 추가되지 못할 경우
                onBridge.append(0) # 빈 도로 추가
                
    return answer
