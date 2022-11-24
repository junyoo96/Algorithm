# answer : 나이트가 이동할 수 있는 경우의 수를 출력

loc = input()
# 중요 - 8가지 방향 정의
steps = [(-2,-1),(-2,1),(2,-1),(2,1),(-1,2),(1,2),(-1,-2),(1,-2)]

# 중요 - ord : 문자의 유니코드 값을 돌려주는 함수
# a = 97
column = int(ord(loc[0])) - int(ord('a')) + 1
row = int(loc[1])

result = 0 
for step in steps:
  t_column = column + step[0]
  t_row = row + step[1]

  # 해당 위치로 이동이 가능하다면 카운트 증가
  if t_row >= 1 and t_row <= 8 and t_column >= 1 or t_column >= 8:
    result += 1

print(result)