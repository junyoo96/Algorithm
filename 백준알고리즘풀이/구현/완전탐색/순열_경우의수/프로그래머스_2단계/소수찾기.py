# 12:14~12:35/12:35~1:15
# =========================
# 최적화 코드
# 주의 - 범위가 넓지 않을 때는 에라토스의 체 말고 기존 소수 구하는 방식 사용하기
#==========================
import math

def check(number):
    if number < 2:
        return False

    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def solution(numbers):
    # dfs 함수(idx, numbers)
    def dfs(idx): # 주의 - 전역변수 사용하면 코드 깔끔하게 안되니까 내장 함수로 구현
        if s:
            current = int(''.join(s))
            nums.add(current)

        # numbers의 개수만큼 반복하면서
        for i in range(len(numbers)):
            # 만약 현재 숫자인덱스를 방문한 적이 없다면
            if not visited[i]:
                # stack에 현재 숫자 추가
                s.append(numbers[i])
                # 방문 여부 True
                visited[i] = True
                # dfs(numbers 몇번째)
                dfs(i)
                # stack에 현재 숫자 pop
                s.pop()
                # 방문 여부 False
                visited[i] = False

    # stack 생성
    s = []
    # 방문여부
    visited = [False] * len(numbers)
    # answer 변수
    nums = set()

    # dfs 함수 호출(idx)
    dfs(0)

    answer = 0
    for num in nums:
        if check(num):
            answer += 1

    return answer

# #=====================================
# 내코드 - 에라토스의체 방식으로 소수 먼저 구해놔서 시간이 오래 걸렸음
# 12:14~12:35/12:35~
# =========================
def solution(numbers):
    # dfs 함수(idx, numbers)
    def dfs(idx):
        # 만약 현재 숫자가 소수라면
        if s:
            current = int(''.join(s))

            if prime[current]:
                # answer 증가
                answer.add(current)

        # numbers의 개수만큼 반복하면서
        for i in range(len(nums)):
            # 만약 현재 숫자인덱스를 방문한 적이 없다면
            if not visited[i]:
                # stack에 현재 숫자 추가
                s.append(nums[i])
                # 방문 여부 True
                visited[i] = True
                # dfs(numbers 몇번째)
                dfs(i)
                # stack에 현재 숫자 pop
                s.pop()
                # 방문 여부 False
                visited[i] = False

    length = len(numbers)
    end = 10 ** length
    # 해당 숫자가 소수인지 아닌지 구하기 0~9999999

    prime = [True] * end
    prime[0] = False
    prime[1] = False
    for i in range(2, int(math.sqrt(end)) + 1):
        for j in range(i * 2, end, i):
            if prime[j]:
                prime[j] = False

    # stack 생성

    s = []
    # 방문여부
    visited = [False] * length
    # answer 변수
    answer = set()

    nums = numbers[:]

    # dfs 함수 호출(idx)
    dfs(0)

    return len(answer)