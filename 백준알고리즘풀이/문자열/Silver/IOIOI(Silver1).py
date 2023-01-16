# 1:47~ 1:57/1:57~ - # 시간초과로 틀림
# 2:00~ 2:15/2:15~ - 아이디어는 생각했지만 IOI만 하는 부분에서 기억안나서 틀림
import sys
input = sys.stdin.readline

# Pn
n = int(input())
# s의 길이
m = int(input())
# Pn이 존재하는지 탐색할 문자열
s = list(input())

# S안에 Pn 몇 군데 포함되어 있는지 개수
answer = 0
# S를 탐색할 때 인덱스
i = 0
# IOI가 몇번 반복되었는지 카운트
count = 0

while i < m - 1:
    if s[i:i+3] == "IOI": # 주의 - Pn과 같은 것이 아니라 IOI하고 같을 때, count변수를 사용해서 횟수를 저장해 같은지 여부를 확인함
        # 다음 I를 향해 건너뛰기
        i += 2
        count += 1

        # 주의 - 만약 현재까지의 count한 문자열이 만약 Pn의 문자열과 일치한다면
        if count == n:
            answer += 1
            # 주의 - 이후 IOI와 일치하는지 확인하기 위해
            count -= 1

    else:
        # IOI와 일치하지 않으므로 인덱스 한칸 이동
        i += 1
        count = 0

print(answer)