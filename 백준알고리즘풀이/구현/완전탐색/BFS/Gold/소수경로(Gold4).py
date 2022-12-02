# 최적화 코드
import math
from collections import deque

# testcase 개수 입력
t = int(input())

# 소수 판별 배열
# 중요 - 에라토스테네스의 체를 사용해 소수 구하기, 범위의 모든 소수를 구할 때 효율적
# 0,1은 소수가 아니므로 False, 이외는 일단 True로 설정
prime_check = [False, False] + [True] * (9998)
# False가 아닌 수(지워지지 않은 수) 중 제일 작은 숫자를 소수로 채택하고, 현재 채택한 숫자의 나머지 배수를 모두 False로 처리(지우기)하는 과정
for i in range(2, int(math.sqrt(10000))): # 중요 - 제곱근 범위까지만 조사, 주의 - math.sqrt 결과값은 float형이므로 int로 형변환 해야함
    # 만약 현재 숫자가 False가 아니라면(지워지지 않은 숫자 중에서)
    if prime_check[i]:
        # 현재 숫자의 나머지 배수를 모두 False 처리(지우기)
        for j in range(2 * i, 10000, i):
            prime_check[j] = False

# testcase 개수 만큼 반복하면서
for _ in range(t):
    # answer
    answer = "Impossible"
    # 시작, 목표 소수 입력
    start, target = map(int, input().split())

    # deque 생성하고 (시작소수,바꾼횟수(1)) 넣기
    queue = deque()
    queue.append((start, 0))

    # 숫자 방문 여부 표시 리스트 생성
    visited = [False] * 10000
    # 현재 숫자 방문처리
    visited[start] = True

    while queue:
        # deque에서 현재소수 popleft
        current, count = queue.popleft()
        # 현재소수 문자로 변환
        str_current = str(current)

        # 만약 현재소수가 목표소수와 같다면
        if current == target:
            answer = count
            break

        # 각 4자리에 0~9를 넣어가며 소수인지 확인
        for i in range(4):
            for j in range(10):
                # 주의 - 각 자리 숫자 변경
                tmp = int(str_current[:i] + str(j) + str_current[i + 1:])

                # 만약 방문한적 없고, 소수이며, 1000이상인 숫자라면
                if not visited[tmp] and prime_check[tmp] and tmp >= 1000:
                    # 방문처리
                    visited[tmp] = True
                    # 해당 소수 queue에 추가
                    queue.append([tmp, count + 1]) # 주의 - 쌍의 형태 데이터를 저장할 때 값을 바꾸는 경우도 있을수 있기 때문에 앞으로, tuple형태가 아닌 리스트로 형태로 넣기

    # answer 출력
    print(answer)

#================================================================================
# 내코드
# 9:21~9:55 / 10:00~11:15 - 구현이 헷갈리는 부분이 있어 디버깅했지만 정답 안보고 풀음

# n (1000~9999)
# 바꾸는 과정에서도 4자리 소수 유지

# 1000만 미만 안됨
# answer : 두 소수 사이에 변환에 필요한 최소 횟수
# bfs 사용해 해결
# ===============================================
from collections import deque

# testcase 개수 입력
t = int(input())
# 1000~9999까지의 리스트(0~10000) 생성해서 소수이면 1, 아니면 0으로 표시
prime_check = [0] * 10000
for i in range(1000, 10000):
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            break
        if j == (i // 2):
            prime_check[i] = 1

# testcase 개수 만큼 반복하면서
for _ in range(t):
    # answer
    answer = "Impossible"
    # 1000~9999까지 방문 여부 표시 리스트 생성
    visited = [0] * 10000

    # 시작, 목표 소수 입력
    start, target = map(int, input().split())
    # deque 생성하고 (시작소수,바꾼횟수(1)) 넣기
    queue = deque()
    queue.append((start, 0))
    # 현재 숫자 방문처리
    visited[start] = 1

    # while True
    while queue:
        # deque에서 현재소수 popleft
        current, count = queue.popleft()
        visited[current] = 1
        # 만약 현재소수가 목표소수와 같다면
        if current == target:
            answer = count
            # break
            break
        # 첫째자리 수 바꾸면서 소수이면 deque에 넣기
        for i in range(1, 10):
            changed = list(str(current))
            # 만약 소수이고 아직 방문하지 않았다면
            changed[0] = str(i)
            changed = int(''.join(changed))
            if prime_check[changed] == 1 and not visited[changed]:
                # deque에 넣기
                queue.append((changed, count + 1))

        # 두째자리 수 바꾸면서 소수이면 deque에 넣기
        for i in range(0, 10):
            changed = list(str(current))
            changed[1] = str(i)
            changed = int(''.join(changed))
            # 만약 소수이고 아직 방문하지 않았다면
            if prime_check[changed] == 1 and not visited[changed]:
                # deque에 넣기
                queue.append((changed, count + 1))

        # 세째자리 수 바꾸면서 소수이면 deque에 넣기
        for i in range(0, 10):
            changed = list(str(current))
            changed[2] = str(i)
            changed = int(''.join(changed))
            # 만약 소수이고 아직 방문하지 않았다면
            if prime_check[changed] == 1 and not visited[changed]:
                # deque에 넣기
                queue.append((changed, count + 1))

        # 넷째자리 수 바꾸면서 소수이면 deque에 넣기
        for i in range(0, 10):
            changed = list(str(current))
            changed[3] = str(i)
            changed = int(''.join(changed))
            # 만약 소수이고 아직 방문하지 않았다면
            if prime_check[changed] == 1 and not visited[changed]:
                # deque에 넣기
                queue.append((changed, count + 1))

    # print(answer)
    print(answer)