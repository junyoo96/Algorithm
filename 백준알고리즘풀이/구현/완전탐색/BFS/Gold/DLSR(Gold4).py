# 내코드
#
# 10:49~11:20 / 11:20~ // 회전구현 틀림
# 계산기
# 명령어
    # D : n을 2배로 바꿔서 9999보다 크면 10000으로 나누고 나머지를 취해서 레지스터에 저장
    # S : n - 1을 레지스터에 저장, n이 0이라면 9999이 저장됨
    # L : 각 자릿수를 왼편으로 회전시켜 저장, (d2,d3,d4,d1)이 됨
    # R : 각 자릿수를 오른편으로 회전시켜 저장, (d4, d1, d2, d3)가 됨

# 레지스터
    # n : 0~9999 십진수 저장
    # n의 4자릿수 d1, d2, d3, d4

# answer : A에서 B로 변환하기 위해 필요한 최소한의 명령어 나열 출력(여러가지면, 아무거나 하나 출력)
# bfs로 풀기
# ======================================================
from collections import deque

def process_command(num, command):
    if command == 'D':
        num = num * 2
        if num > 9999:
            num %= 10000
    elif command == 'S':
        num -= 1
        if num == 0:
            num = 9999
    elif command == 'L': # 왼쪽으로 회전
        # str_num = list(str(num))
        # list_num = ['0'] * (4 - len(str_num)) + str_num
        # tmp_num = ['0'] * 4
        #
        # for i in range(3, -1, -1):
        #     tmp_num[(i - 1) % 4] = list_num[i]

        front = num % 1000
        back = num // 1000
        num = front * 10 + back

    else: # 오른쪽으로 회전
        # str_num = list(str(num))
        # list_num = ['0'] * (4 - len(str_num)) + str_num
        # tmp_num = ['0'] * 4
        #
        # for i in range(4):
        #     tmp_num[(i + 1) % 4] = list_num[i]
        #
        # num = int("".join(tmp_num))

        front = num % 10
        back = num // 10
        num = front * 1000 + back

    return num

# tescase 개수 입력
t = int(input())
# testcase를 반복하면서
for _ in range(t):
    # answer 변수
    answer = ""
    # 시작수, 목표수 입력
    start, target = map(int, input().split())
    # 방문 여부 리스트
    visited = [False] * 10000

    # deque 생성
    queue = deque()
    # deque에 [현재수, 현재 카운트, 현재까지 진행한 명령어] 추가
    queue.append([start, 0, ""])
    # 현재수 방문처리
    visited[start] = True

    # while deque:
    while queue:
        # deque에서 popleft
        current, count, processed_command = queue.popleft()
        # 만약 원소의 현재수가 목표수와 같다면
        if current == target:
            # answer = 현재까지 진행한 명령어
            answer = processed_command
            # break
            break

        # 명령어 4가지를 반복하면서
        for command in ['D', 'S', 'L', 'R']:
            # 변경된 수 = 커맨드 함수 호출(현재 수, 명령어)
            changed_num = process_command(current, command)
            # 만약 변경된 수를 방문한적이 없다면
            if not visited[changed_num]:
                # deque에 추가[변경된수, 현재카운트 + 1, 현재까지 진행한 명령어]
                queue.append([changed_num, count + 1, processed_command + command])
                # 변경된수 방문처리
                visited[changed_num] = True

    # answer 출력
    print(answer)

#=============================================
# 최적화 코드
import sys
from collections import deque

input = sys.stdin.readline


def process_command(num, command):
    if command == 'D':
        num = num * 2 % 10000
    elif command == 'S':
        num -= 1
        if num < 0:
            num = 9999
    elif command == 'L': # 중요 - 왼쪽으로 회전
        front = num % 1000
        back = num // 1000
        num = front * 10 + back

    else: # 중요 - 오른쪽으로 회전
        front = num % 10
        back = num // 10
        num = front * 1000 + back

    return num


# tescase 개수 입력
t = int(input())
# testcase를 반복하면서
for _ in range(t):
    # answer 변수
    answer = ""
    # 시작수, 목표수 입력
    start, target = map(int, input().split())
    # 방문 여부 리스트
    visited = [False] * 10000

    # deque 생성
    queue = deque()
    # deque에 [현재수, 현재 카운트, 현재까지 진행한 명령어] 추가
    queue.append([start, ""])
    # 현재수 방문처리
    visited[start] = True

    # while deque:
    while queue:
        # deque에서 popleft
        current, processed_command = queue.popleft()
        # 만약 원소의 현재수가 목표수와 같다면
        if current == target:
            # answer = 현재까지 진행한 명령어
            answer = processed_command
            # break
            break

        # 명령어 4가지를 반복하면서
        for command in ['D', 'S', 'L', 'R']:
            # 변경된 수 = 커맨드 함수 호출(현재 수, 명령어)
            changed_num = process_command(current, command)
            # 만약 변경된 수를 방문한적이 없다면
            if not visited[changed_num]:
                # deque에 추가[변경된수, 현재카운트 + 1, 현재까지 진행한 명령어]
                queue.append([changed_num, processed_command + command])
                # 변경된수 방문처리
                visited[changed_num] = True

    # answer 출력
    print(answer)
