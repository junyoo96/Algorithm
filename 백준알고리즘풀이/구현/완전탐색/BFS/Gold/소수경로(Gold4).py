# 9:21~9:55 / 10:00~11:15 - 구현이 헷갈리는 부분이 있어 디버깅했지만 정답 안보고 풀음(에라토스테네스의 체 모를 때 풀은거)
# 11:14~11:35 / 11:35~12:12 - 에라토스테네스의 체 사용해서 제대로 풀음

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
# 11:14~11:35 / 11:35~12:12

# 네자리 소수만 주어진다고 가정(1000~9999)
# 바꾸는 과정에서도 소수여야되고, 1000미만이면 안됨
# answer : 두 소수 사이의 변환에 필요한 최소 횟수 출력
# 불가능한 경우 Impossible 출력
# ==============================================
import math
from collections import deque

# 0~9999까지의 소수 계산 리스트 생성(True)
primes = [True] * 10000
# 0, 1은 False
primes[0] = False
primes[1] = False
# 2부터 9999까지 반복하면서
for i in range(2, int(math.sqrt(10000))):
    # 현재수의 2배부터 9999까지 배수만큼 건너띄면서 반복하면서
    for j in range(i * 2, 10000, i):
        # 만약 방문하는 수가 리스트에서 True라면
        if primes[j]:
            # 방문하는 수에 대해 False로 바꾸기
            primes[j] = False

# t입력
t = int(input())
# t를 반복하면서
for _ in range(t):
    # a,b 입력
    a, b = map(int, input().split())
    # deque 생성 # deque에 (시작숫자, 바꾼횟수) 추가
    queue = deque([(a, 0)])
    # 방문리스트 생성(9999)
    visited = [False] * 10000
    # 시작숫자 방문처리
    visited[a] = True

    answer = 0
    # while True
    while queue:
        # 현재숫자, 바꾼횟수 = deque에서 꺼내기
        num, change = queue.popleft()
        # print(num, change)
        # 만약 현재 숫자가 b라면
        if num == b:
            # answer = 바꾼횟수
            answer = change
            # break
            break

        # 첫번째자리(1~9)
        for i in range(1, 10):
            tmp = str(num)
            changed_num = int(str(i) + tmp[1:])
            # 만약 해당 자리 바꾼 수를 방문한적이 없고 소수라면
            if not visited[changed_num] and primes[changed_num]:
                # deque에 (바꾼숫자, 바꾼횟수 + 1) 추가
                queue.append((changed_num, change + 1))
                visited[changed_num] = True

        # 두번째,세번째, 네번째 자리(0~9)
        for i in range(10):
            tmp = str(num)
            changed_num = int(tmp[0] + str(i) + tmp[2:])
            # 만약 해당 자리 바꾼 수를 방문한적이 없고 소수라면
            if not visited[changed_num] and primes[changed_num]:
                # deque에 (바꾼숫자, 바꾼횟수 + 1) 추가
                queue.append((changed_num, change + 1))
                visited[changed_num] = True

        for i in range(10):
            tmp = str(num)
            changed_num = int(tmp[:2] + str(i) + tmp[-1])
            # 만약 해당 자리 바꾼 수를 방문한적이 없고 소수라면
            if not visited[changed_num] and primes[changed_num]:
                # deque에 (바꾼숫자, 바꾼횟수 + 1) 추가
                queue.append((changed_num, change + 1))
                visited[changed_num] = True

        for i in range(10):
            tmp = str(num)
            changed_num = int(tmp[:-1] + str(i))
            # 만약 해당 자리 바꾼 수를 방문한적이 없고 소수라면
            if not visited[changed_num] and primes[changed_num]:
                # deque에 (바꾼숫자, 바꾼횟수 + 1) 추가
                queue.append((changed_num, change + 1))
                visited[changed_num] = True

    if answer == 0 and not visited[b]:
        print("Impossible")
    else:
        print(answer)