# 12:25~2:03 / 2:03~

# n : 벨트 수
# m : 물건 수

# 1. 공장설립
    # 선물의 번호는 오르차순으로 벨트에 쌓임
# 2. 물건 모두 옮기기
    # m_src 벨트의 선물을 m_dst 벨트의 맨 앞에 위치시킴(m_src과 m_dst는 같지않음)
    # 옮긴 후 m_dst번째 벨트에 있는 선물 개수 출력
# 3. 앞 물건만 교체
    # m_src 벨트의 맨 앞 선물을 m_dst 벨트의 맨 앞 선물과 교체
    # 존재하지 않는 경우 해당 벨트로 선물만 옮김
    # 옮긴 후 m_dst번째 벨트에 있는 선물 개수 출력
# 4. 물건 나누기
    # m_src의 가장 앞에서 floor(n/2)번까지의 선물들을 m_dst번째 벨트 앞으로 옮김
    # n : m_src번째 벨트에 있는 선물들 개수
    # 만약 m_src 벨트에 선물이 1개인 경우에는 옮기지 않음
    # 옮긴 뒤 m_dst번째 벨트에 있는 선물들 개수 출력
# 5. 선물 정보 얻기
    # 선물번호 p_num에 대해, 해당 선물의 앞 선물 번호 a와 뒤 선물번호 b라 할 때, a + 2 * b 출력
    # 만약 앞 선물이 없는 경우 a = -1, 뒤 선물이 없는 경우에는 b = -1을 넣어줌
# 6. 벨트 정보 얻기
    # 벨트 번호 b_num에 대해, a + 2 * b + 3 * c 출력
    # a : 해당 벨트 맨 앞 선물 번호
    # b : 해당 벨트 맨 뒤 선물 번호
    # c : 해당 벨트 모든 선물 개수

# 선물이 없는 밸트인 경우 a, b 모두 -1

# q : 명령어 수
# answer : 출력해야 하는 값 하나씩 출력
#=======================================================
MAX_N = 100000
MAX_M = 100000

# 변수 선언
n, m, q = -1, -1, -1

# id에 해당하는 상자의 nxt값과 prv값을 관리
# 0이면 없다는 뜻
# 중요 - 이전 산타 문제와 다르게 리스트로 처리함
prv, nxt = [0] * (MAX_M + 1), [0] * (MAX_M + 1)

# 각 벨트별로 head, tail id, 그리고 총 선물 수를 관리
# 0이면 없다는 뜻
# 중요 - 선물 수 관리 만 진행
head, tail, num_gift = [0] * MAX_N, [0] * MAX_N, [0] * MAX_N

# 공장 설립
def build_factory(elems):
    # 공장 정보를 입력
    n, m = elems[1], elems[2]

    # 벨트별로 물건 id 저장
    boxes = [[] for _ in range(n)]
    for _id in range(1, m + 1):
        b_num = elems[_id + 2] # 3~끝까지
        b_num -= 1 # 벨트 번호 0부터 시작하기 위해

        boxes[b_num].append(_id)

    # 초기 벨트의 head, tail, nxt, prv값을 설정
    # 벨트 수 만큼 반복하면서
    for i in range(n):
        # i : 벨트 idx
        # 비어있는 벨트라면 패스
        if len(boxes[i]) == 0:
            continue

        # 벨트의 head, tail을 설정
        head[i] = boxes[i][0]
        tail[i] = boxes[i][-1]

        # 벨트 내 선물 총 수를 관리
        num_gift[i] = len(boxes[i])

        # nxt, prv를 설정
        for j in range(len(boxes[i]) - 1):
            nxt[boxes[i][j]] = boxes[i][j + 1]
            prv[boxes[i][j + 1]] = boxes[i][j]

# 물건을 전부 이동 함수
def move(elems):
    m_src, m_dst = elems[1] - 1, elems[2] - 1 # 벨트 0부터 시작하므로 -1

    # 만약 m_src에 물건이 없다면, 그대로 m_dst내 물건 수가 답이됨
    if num_gift[m_src] == 0:
        print(num_gift[m_dst])
        return

    # 만약 m_dst에 물건이 없다면, 그대로 옮겨줌
    if num_gift[m_dst] == 0:
        # 목표 벨트의 head를 출발 벨트의 head로 변경
        head[m_dst] = head[m_src]
        # 목표 벨트의 tail을 목표 벨트의 tail로 변경
        tail[m_dst] = tail[m_src]
    # 만약 m_dst에 물건이 있다면
    else:
        # 목표 벨트의 원래 head
        orig_head = head[m_dst]
        # 목표 벨트의 head를 출발 벨트의 head로 교체
        head[m_dst] = head[m_src]
        # 출발 벨트의 tail과 기존 목표 벨트의 head를 연결
        src_tail = tail[m_src]
        nxt[src_tail] = orig_head
        prv[orig_head] = src_tail

    # 출발 벨트의 물건을 전부 이동했으므로 출발 벨트의 head, tail을 비우기
    head[m_src] = tail[m_src] = 0

    # 선물 상자 수를 갱신
    num_gift[m_dst] += num_gift[m_src]
    num_gift[m_src] = 0

    # 목표 벨트의 선물 수 출력
    print(num_gift[m_dst])

# 중요 - 해당 벨트의 head를 제거
def remove_head(b_num):
    # 불가능하면 패스(해당 벨트에 아무 선물도 없는 경우)
    if not num_gift[b_num]:
        return 0

    # 만약 해당 벨트에 선물이 1개라면, head, tail 전부 삭제 후 반환
    if num_gift[b_num] == 1:
        _id = head[b_num]
        # 해당 벨트의 head, tail 전부 삭제
        head[b_num] = tail[b_num] = 0
        # 제거했으므로 선물 수 0으로 갱신
        num_gift[b_num] = 0
        return _id

    # 만약 해당 벨트에 선물이 2개이상이라면, 기존 head제거하고 다음 선물로 head를 바꾸기
    hid = head[b_num]
    next_head = nxt[hid]
    # 기존 head와 다음 선물과의 연결 제거
    nxt[hid] = prv[next_head] = 0
    # 선물 수 감소
    num_gift[b_num] -= 1
    # 헤드 변경
    head[b_num] = next_head

    return hid

# 중요 - 해당 밸트에 head를 추가
def push_head(b_num, hid):
    # 불가능한 경우는 진행하지 않음(주어진 hid가 0이라면 추가할 선물이 없다는 의미
    if hid == 0:
        return

    # 만약 해당 벨트가 비어있었다면, head, tail을 동시에 추가
    if not num_gift[b_num]:
        head[b_num] = tail[b_num] = hid
        # 선물 수 증가
        num_gift[b_num] = 1
    # 만약 해당 벨트가 비어있지 않다면, head만 교체
    else:
        orig_head = head[b_num]
        nxt[hid] = orig_head
        prv[orig_head] = hid
        # 해당 벨트의 head를 주어진 선물로 교체
        head[b_num] = hid
        # 선물 수 증가
        num_gift[b_num] += 1

# 앞 물건을 교체
def change(elems):
    m_src, m_dst = elems[1] - 1, elems[2] - 1

    # 출발 벨트의 헤드 제거
    src_head = remove_head(m_src) # src_head : 제거한 선물 id
    # 목표 벨트의 헤드 제거
    dst_head = remove_head(m_dst) # dst_head : 제거한 선물 id
    # 목표 벨트에 출발 벨트의 헤드 추가
    push_head(m_dst, src_head)
    # 출발 벨트에 목표 벨트의 헤드 추가
    push_head(m_src, dst_head)

    # 목표 벨트의 선물 수 출력
    print(num_gift[m_dst])

# 물건을 나눠옮기기
def divide(elems):
    m_src, m_dst = elems[1] - 1, elems[2] - 1

    # 순서대로 src에서 박스들을 빼기
    # 출발 벨트의 선물 수
    cnt = num_gift[m_src]
    # 뺀 선물의 id 저장 리스트
    box_ids = []
    # 선물수 // 2 개수만큼의 선물을 출발벨트에서 빼고 뺀 선물의 id를 저장
    for _ in range(cnt // 2):
        box_ids.append(remove_head(m_src))

    # 거꾸로 뒤집어서 하나씩 목표 벨트에 선물들을 넣어줌
    for i in range(len(box_ids) - 1, -1, -1):
        push_head(m_dst, box_ids[i])

    # 목표 벨트의 선물 수 출력
    print(num_gift[m_dst])

# 선물 점수를 얻기
def gift_score(elems):
    p_num = elems[1]

    # 중요 - if else 처리 사용법
    a = prv[p_num] if prv[p_num] != 0 else -1
    b = nxt[p_num] if nxt[p_num] != 0 else -1

    print(a + 2 * b)


# 벨트 정보를 얻기
def belt_score(elems):
    b_num = elems[1] - 1

    a = head[b_num] if head[b_num] != 0 else -1
    b = tail[b_num] if tail[b_num] != 0 else -1
    c = num_gift[b_num]

    print(a + 2 * b + 3 * c)


# 입력
q = int(input())
for _ in range(q):
    elems = list(map(int, input().split()))
    action = elems[0]

    if action == 100:
        build_factory(elems) # 공장 설립
    elif action == 200:
        move(elems) # 물건 모두 옮기기
    elif action == 300:
        change(elems) # 앞 물건만 교체
    elif action == 400:
        divide(elems) # 물건 나누기
    elif action == 500:
        gift_score(elems) # 선물 정보 얻기
    else:
        belt_score(elems) # 벨트 정보 얻기