#상하좌우(p.112) 
#O(N)

# 입력
# n : 5
# plans : R R R U D Dcde fg

# 출력

n = int(input())
x, y= 1, 1
plans = input().split()

#L,R,U,D에 따른 이동방향
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

#이동계획을 확인
for plan in plans:
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
      
  if nx<1 or ny<1 or nx>n or ny>n: #공간을 벗어나는 경우 무시 
    continue
    
  x, y = nx, ny #이동수행 
    
print(x, y)
