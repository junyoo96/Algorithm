# 10:06~10:29/ 10:54~12:00(89분) - 풀긴풀었지만 idle사용해서 풀음
# 3:48~3:57/3:57~4:14

# 암호
    # L개의 알파벳 소문자
    # 최소 1개 모음 + 최소 2개 자음으로 구성
    # 알파벳이 증가하는 순서로 배열
# c : 조교들이 암호로 사용했을 법한 문자 종류의 개수
# answer : 가능성 있는 암호들을 모두 구하기
#============================================================
# 최적화 코드(백트래킹 방식)
# cnt : 현재 알파벳의 길이(주어진 암호길이가 됐는지 확인위해 사용)
# idx : 몇번째 알파벳을 추가해야하는지 위해 사용
def back_tracking(cnt, idx):

    # 1. 탐색 중지하기 위한 조건 체크
    # 만약 암호를 만들은 경우
    if cnt == l:
        vo = 0
        co = 0

        # 모음, 자음 조건 맞는지 확인
        for i in range(l):
            if answer[i] in vowel:
                vo += 1
            else:
                co += 1

        # 만약 조건이 맞다면 출력
        if vo >= 1 and co >= 2:
            # 주의 - list를 string으로 변환
            print("". join(answer))

        # 조건에 맞지 않다면 return(탐색 종료)
        return

    # 반복문을 통해 암호를 만들기
    for i in range(idx, c):
        # 2. stack 기반의 DFS 방식 탐색
        # 알파벳 추가
        answer.append(alphabets[i])
        back_tracking(cnt + 1, i + 1)
        # 조건검사 후 이전 노드로 돌아오기
        answer.pop()

# answer 리스트
answer = []
# L, C 입력
l, c = map(int, input().split())
# 문자 종류 입력
alphabets = sorted(list(input().split()))  # 주의 - split써야되는지 말야야되는지 헷갈렸음
vowel = ['a', 'e', 'i', 'o', 'u']

back_tracking(0, 0)

#=================================================================
# 내코드(BFS 방식)
from collections import deque

# answer 리스트
answer = []
# L, C 입력
l, c = map(int, input().split())
# 문자 종류 입력
alphabets = list(input().split()) # 주의 - split써야되는지 말야야되는지 헷갈렸음
alphabets.sort()

# 모음자음 체크 함수(문자리스트)
def alphabet_check(password):
    # 모음 리스트 (a,e,i,o,u)
    mo = ['a', 'e', 'i', 'o', 'u']
    # 모음 카운트 변수
    mo_count = 0
    # 자음 카운트 변수
    ja_count = 0
    # 문자리스트를 반복하면서
    for p in password:
        # 만약 현재 문자가 모음리스트에 있다면
        if p in mo:
            # 모음 카운트 증가
            mo_count += 1
        # else
        else:
            # 자음 카운트 증가
            ja_count += 1

    # 만약 모음이 1개이상이고 자음이 2개이상이면
    if mo_count >= 1 and ja_count >= 2:
        # return True
        return True

    # retrun False
    return False


# deque 생성
queue = deque()
# deque에 현재 알파벳들과 방문여부 리스트 추가
for i in range(len(alphabets)):
    alphabet_list = []
    alphabet_list.append(alphabets[i])
    visited = [False] * len(alphabets)
    visited[i] = True
    queue.append((alphabet_list, visited))

# while deque:
while queue:
    # 현재 알파벳 리스트, 방문여부 리스트= deque에서 popleft
    alphabet_list, visited = queue.popleft()

    # 만약 현재 알파벳의 길이가 l과 같다면
    if len(alphabet_list) == l:
        # 만약 모음자음 체크 함수(알파벳) true이면
        if alphabet_check(alphabet_list):
            # answer에 현재알파벳들을 문자열 형태로 추가
            answer.append(''.join(alphabet_list))
            # continue
            continue

    # alphabet 종류만큼 반복하면서
    for i in range(len(alphabets)):
        # 만약 아직 방문하지 않았고
        if not visited[i]:
            # 방문가능한 알파벳이 현재 알바벳의 마지막 알파벳보다 크다면
            if alphabets[i] > alphabet_list[-1]:
                # deque에 (현재 알파벳 리스트 + 추가된 알파벳, 현재 알파벳을 방문처리한 방문여부 리스트)
                visited[i] = True
                queue.append((alphabet_list + list(alphabets[i]), visited))
                visited[i] = False

# answer 리스트를 반복하면서
for a in answer:
    # 요소 출력
    print(a)