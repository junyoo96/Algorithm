#시각(p.113)

#input : 5
#output : 11475

#시간 입력받기 
h = int(input())
answer = 0 

for i in range(h+1):
  for j in range(60):
    for m in range(60):
      if '3' in str(i)+str(j)+str(m): #매 시각 안에 '3' 이 포함되면 카운트 
        answer += 1
        
print(answer)




        
