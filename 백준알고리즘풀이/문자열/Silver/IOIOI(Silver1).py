# 1:47~ 1:57/1:57~ - # 시간초과로 틀림
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
    if s[i:i+3] == "IOI":
        # 다음 I를 향해 건너뛰기
        i += 2
        count += 1

        # 만약 현재까지의 count한 문자열이 만약 Pn의 문자열과 일치한다면
        if count == n:
            answer += 1
            # 이후 IOI와 일치하는지 확인하기 위해
            count -= 1

    else:
        # IOI와 일치하지 않으므로 인덱스 한칸 이동
        i += 1
        count = 0

print(answer)