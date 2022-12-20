# 최적화 코드

# q : 명령 수
# 일 종류
    # 1. 공장설립
        # 선물 공장 m개의 벨트 설치
        # 각 벨트 위에 정확히 n/m개의 물건들이 놓아 총 n개의 물건을 준비
        # 물건
        # 번호 ID, 무게 w 가 적혀있음
        # 번호는 상자마다 다름
        # 무게는 동일할 수 있음
    # 2. 물건하차
        # 상자 최대 무게 w_max
        # 벨트의 맨앞부터 선물의 무게가 w_max이하라면 하차 진행
        # 아니라면, 벨트 맨 뒤로 보냄
        # 벨트에 있던 상자가 빠지면 한칸씩 앞으로 내려와야함
        # 하차된 상자의 무게의 총합을 print
    # 3. 물건제거
        # 산타가 제거하기를 원하는 물건의 고유 번호 r_id
        # 해당 벨트에서 상자를 제거하고 이에 있던 상자들은 앞으로 한칸씩 내려옴
        # 그러한 상자가 있다면 r_id값 출력, 없다면 -1 print
    # 4. 물건확인
        # 산타가 확인하기를 원하는 물건의 고유번호 f_id
        # 해당 고유 번호에 해당하는 상자가 놓여있는 벨트가 있다면 해당 벨트의 번호를 출력, 없다면 -1 출력
        # 상자가 있는 경우, 해당 상자 위에 있는 모든 상자를 전부 앞으로 가져옴(맨 뒤에 있는 것을 맨 앞으로)
        # 가져올시 순서를 그대로 유지
    # 5. 고장이 발생한 벨트의 번호 b_num
        # 해당 벨트는 다시 사용할 수 없음
        # 벨트의 바로 오른쪽 벨트부터 순서대로 보며 아직 고장이 나지않은 최초의 벨트 위올 b_num 벨트에 놓여있던 상자들을 아래에서부터 순서대로 하나씩 옮김
        # 단, 모든 벨트가 망가지는 경우는 없음
        # 만약 b_num 벨트가 이미 망가져있다면 -1, 그렇지 않았다면 b_num 값 출력

# answer:  q번에 걸쳐 명령을 순서대로 진행했을 때 원하는 결과를 출력
# 리스트 자료구조의 함수를 직접 구현하는 문제라고 생각하고 풀기
#================================================================

from collections import defaultdict

MAX_M = 10

# 변수 선언
# n : 박스 수
# m : 벨트 수
# q : 명령 수
n, m, q = -1, -1, -1

# 각 id별로 상자 무게를 저장
weight = {}

# id에 해당하는 상자의 nxt값과 prv값을 관리
    # nxt = {현재 상자id : 현재 상자의 다음상자 id} 형식으로 구성
    # prv = {현재 상자id : 현재 상자의 이전상자 id} 형식으로 구성
    # 0이면 없다는 뜻
prv, nxt = defaultdict(lambda: 0), defaultdict(lambda: 0)

# 각 벨트별로 head(해당 벨트의 첫번째 박스 id), tail(해당 벨트의 마지막 박스 id) id를 관리
# 0이면 없다는 뜻
head = [0] * MAX_M
tail = [0] * MAX_M

# 벨트가 망가졌는지 여부
broken = [False] * MAX_M

# 물건 별로 벨트 번호를 기입
# 벨트 번호가 -1이면 사라진 것
belt_num = defaultdict(lambda: -1)

# 공장 설립
def build_factory(elems):
    global n, m

    # 박스 수, 벨트 수 입력
    n, m = elems[1], elems[2]
    # 박스 id, 무게 입력
    ids, ws = elems[3:3 + n], elems[3 + n:3 + n + n]

    # id마다 무게를 관리
    for i in range(n):
        weight[ids[i]] = ws[i]

    # 벨트 별로 상자 목록을 넣어줌
    size = n // m # 벨트마다 넣어줄 물건 개수
    # 벨트 개수 만큼 반복하면서
    for i in range(m):
        # 벨트 마다의 head, tail을 설정
        head[i] = ids[i * size] # 해당 벨트의 첫번재 박스 id 저장
        tail[i] = ids[(i + 1) * size - 1] # 해당 벨트의 마지막 박스 id 저장
        # 해당 벨트의 첫번째 박스부터 마지막 박스까지 반복하면서
        for j in range(i * size, (i + 1) * size):
            # 상자 ID마다 벨트 번호를 기입
            belt_num[ids[j]] = i

            # nxt, prv를 설정
            if j < (i + 1) * size - 1:
                nxt[ids[j]] = ids[j + 1]
                prv[ids[j + 1]] = ids[j]

# Id에 해당하는 상자를 삭제
# _id : 삭제할 상자 id
def remove_id(_id, remove_belt):
    b_num = belt_num[_id]
    # 벨트 번호를 제거
    if remove_belt:
        belt_num[_id] = -1

    # 만약 해당 벨트에 박스가 하나 남았다면(해당 벨트의 첫번째 상자id와 마지막 상자id가 같다면 하나만 남았다는 의미이므로)
    if head[b_num] == tail[b_num]:
        # 0이면은 없다는 의미이므로 0으로 설정
        head[b_num] = tail[b_num] = 0

    # 만약 삭제 될 박스가 벨트의 맨 앞에 있다면(head) ,head만 변경되고 끝남
    elif _id == head[b_num]:
        # 삭제될 박스의 다음 박스 id
        nid = nxt[_id]
        # 현재 벨트의 맨 앞 박스를 다음 박스 id로 갱신
        head[b_num] = nid
        # 다음 박스의 이전 박스는 이제 없으므로 0으로 설정
        prv[nid] = 0
    # 만약 삭제 될 박스가 벨트의 맨 뒤에 있다면(tail) ,tail만 변경되고 끝남
    elif _id == tail[b_num]:
        # 삭제될 박스의 이전 박스 id
        pid = prv[_id]
        # 현재 벨트의 맨 뒤 박스를 이전 박스 id로 갱신
        tail[b_num] = pid
        # 이전 박스의 다음 박스는 이제 없으므로 0으로 설정
        nxt[pid] = 0
    # 만약 중간에 있는 박스가 삭제되는 것이라면, nxt, prv만 수선해줍니다.
    else:
        # 현재 박스의 이전 박스 id, 현재 박스의 다음 박스 id
        pid, nid = prv[_id], nxt[_id]
        # 이전 박스의 다음박스는 nid로 갱신
        nxt[pid] = nid
        # 다음 박스의 이전박스는 pid로 갱신
        prv[nid] = pid

    # nxt, prv값을 지워줌
    nxt[_id] = prv[_id] = 0

# target_id 바로 뒤에 id를 추가하는 함수
def push_id(target_id, _id):
    # target_id 박스 뒤에 _id 박스 추가
    nxt[target_id] = _id
    # _id박스 앞에 target_id 박스 추가
    prv[_id] = target_id

    # target_id 박스가 위치한 벨트 확인
    b_num = belt_num[target_id]
    # 만약 target_id가 tail이었다면(해당 벨트의 맨 마지막에 있었다면), tail을 변경
    if tail[b_num] == target_id:
        # 해당 벨트의 맨 마지막 박스를 _id로 변경
        tail[b_num] = _id

# 물건 하차
def drop_off(elems):
    # 하차 기준 무게
    w_max = elems[1]

    # 각 벨트를 반복하면서 첫 번째 상자를 확인
    w_sum = 0
    for i in range(m):
        # 망가진 벨트라면 패스
        if broken[i]:
            continue

        # 만약 벨트에 박스가 있다면
        if head[i] != 0:
            # 해당 벨트의 첫번재 박스의 id
            _id = head[i]
            # 해당 벨트의 첫번재 박스의 무게
            w = weight[_id]

            # 가장 앞에 있는 상자의 무게가 w_max 이하라면, 하차시키고 무게 합에 더해줌
            if w <= w_max:
                w_sum += w

                # 하차를 진행
                remove_id(_id, True)
            # 만약 그렇지 않다면 상자를 벨트의 맨 뒤로 올려줌
            elif nxt[_id] != 0:
                # 현재 위치에서 제거하고
                remove_id(_id, False)
                # 맨 뒤에 push
                push_id(tail[i], _id)

    # 하차한 상자의 무게 합을 출력합니다.
    print(w_sum)

# 물건 제거
def remove(elems):
    # 제거할 박스 id
    r_id = elems[1]

    # 만약 이미 삭제된 상자라면, -1을 출력하고 패스
    if belt_num[r_id] == -1:
        print(-1)
        return

    # 아니라면 해당 상자를 제거
    remove_id(r_id, True)
    # 제거할 박스 id 출력
    print(r_id)

# 물건 확인
def find(elems):
    # 찾을 상자 id
    f_id = elems[1]

    # 만약 이미 삭제된 상자라면, -1을 출력하고 패스
    if belt_num[f_id] == -1:
        print(-1)
        return

    # 해당 상자가 위치한 벨트 번호
    b_num = belt_num[f_id]

    # 만약 해당 상자가 맨 앞 상자가 아니라면(맨 앞에 이미 위치하고 있다면 맨앞으로 당길 필요가 없음)
    if head[b_num] != f_id:
        # 해당 벨트의 원래 맨 뒤 상자 id
        orig_tail = tail[b_num]
        # 해당 벨트의 원래 맨 앞 상자 id
        orig_head = head[b_num]

        # 확인한 상자의 앞상자 (확인한 상자를 포함해 위에 있던 상자까지 모두 맨 앞으로 이동함으로, 확인한 상자 앞에 있던 상자가 tail이됨)
        now_tail = prv[f_id]
        # 새로 tail을 갱신
        tail[b_num] = now_tail
        # tail이 되었음으로 뒤에 상자가 없기때문에 0으로 설정
        nxt[now_tail] = 0

        # 기존 tail의 nxt를 기존의 head로, head의 prv를 기존 tail로 만들어줌
        nxt[orig_tail] = orig_head
        prv[orig_head] = orig_tail

        # 찾은 상자 id로 새로운 head를 갱신
        head[b_num] = f_id

    # 해당 ID의 belt 번호를 출력합니다.
    print(b_num + 1)


# 벨트 고장
def broken_belt(elems):
    # 고장난 벨트 번호
    b_num = elems[1]
    b_num -= 1

    # 만약 해당 벨트가 이미 망가져 있다면, -1을 출력하고 패스
    if broken[b_num]:
        print(-1)
        return

    # 현재 벨트 고장났다고 표시
    broken[b_num] = 1

    # 만약 빈 벨트라면 패스
    if head[b_num] == 0:
        print(b_num + 1)
        return

    # 오른쪽으로 돌면서 아직 망가지지 않은 벨트 위로 상자를 전부 옮겨주기
    nxt_num = b_num # 현재 확인할 벨트번호
    while True:
        # 현재 확인할 벨트번호가 벨트 개수를 넘지않도록 처리
        nxt_num = (nxt_num + 1) % m
        # 만약 최초로 망가지지 않은 곳이라면
        if not broken[nxt_num]:
            # 만약 해당 벨트가 비어있다면, 그대로 옮기기
            if tail[nxt_num] == 0:
                head[nxt_num] = head[b_num]
                tail[nxt_num] = tail[b_num]
            # 해당 벨트가 비어있지 않다면
            else:
                # 해당 위치로 상자를 전부 옮겨주기
                # 고장난 벨트의 head만 옮길 벨트의 tail뒤에 붙여준 뒤
                push_id(tail[nxt_num], head[b_num])
                # 옮길 벨트의 tail만 고장난 벨트의 tail로 바꾸기
                tail[nxt_num] = tail[b_num]

            # 고장난 벨트의 head부터 tail까지 반복하면서 belt_num을 갱신(다른 벨트로 상자를 옮겼음으로)
            _id = head[b_num] # 고장난 벨트의 맨 앞 상자 id
            while _id != 0: # 마지막 상자까지 반복하면서
                # 고장난 벨트의 상자들의 belt 번호를 갱신
                belt_num[_id] = nxt_num
                # 다음상자로 이동
                _id = nxt[_id]

            # 고장난 벨트에 아무것도 없으므로 고장난 벨트의 head와 tail 0으로 초기화
            head[b_num] = tail[b_num] = 0
            break

    # 벨트 번호 출력
    print(b_num + 1)

# 입력:
q = int(input())
for _ in range(q):
    elems = list(map(int, input().split()))
    command = elems[0]

    if command == 100:
        build_factory(elems)
    elif command == 200:
        drop_off(elems)
    elif command == 300:
        remove(elems)
    elif command == 400:
        find(elems)
    else:
        broken_belt(elems)

#=================================================================
# 틀린코드 - queue로 구현하려고 시도
# 10:50~11:35 / 구현 11:41~12:41 / 디버깅12:41~

from collections import deque


# 공장설립 함수
def create_factory(command):
    # n = 입력의 1번째
    n = command[1]
    # m = 입력의 2번째
    m = command[2]
    # 1*m 만큼의 이중리스트 생성(deque)
    for _ in range(m):
        queue = deque()
        belts.append(queue)

    # id 리스트 = 입력받은것의[3:3+n]
    ids = command[3:3 + n]
    # 무게 리스트 = 입력받은것의[3+n+:]
    weights = command[3 + n:]

    belt_idx = 0
    # 1부터 n만큼 반복하면서
    for i in range(1, n + 1):
        belts[belt_idx].append((ids[i - 1], weights[i - 1]))

        # 만약 현재 index가 n/m과 같다면
        if i % (n / m) == 0:
            # 현재 벨트에 (id, weight)추가
            belt_idx += 1

    return n, m


# 물건하차 함수
def down_box(command):

    # w_max = 입력 1번째값
    w_max = command[1]

    # 벨트의 맨앞의 선물의 무게가 w_max이하라면 하차 진행
    # 아니라면, 벨트 맨 뒤로 보냄
    down_weight_sum = 0

    for i in range(m):
        if belts[i] is not None:
            if belts[i]:
                id, weight = belts[i].popleft()

                if weight > w_max:
                    belts[i].append((id, weight))
                if weight <= w_max:
                    down_weight_sum += weight

    # for belt in belts:
    #     print("확인", belt)

    # 하차된 상자의 무게의 총합을 print
    print(down_weight_sum)

# 물건제거 함수
def remove_box(command):
    # r_id = 입력 1번째값
    r_id = command[1]
    # 해당 벨트에서 상자를 제거하고 이에 있던 상자들은 앞으로 한칸씩 내려옴
    # 그러한 상자가 있다면 r_id값 출력, 없다면 -1 print

    for i in range(m):
        if belts[i] is not None:

            length = len(belts[i])
            for j in range(length):
                if belts[i][j][0] == r_id:
                    belt = list(belts[i])
                    belt.pop(j)
                    belts[i] = deque(belt)

                    print(r_id)

                    return

    print(-1)


# 물건확인 함수
def check_box(command):
    # r_id = 입력 1번째값
    r_id = command[1]
    # 해당 고유 번호에 해당하는 상자가 놓여있는 벨트가 있다면 해당 벨트의 번호를 출력, 없다면 -1 출력
    # 상자가 있는 경우, 해당 상자 위에 있는 모든 상자를 전부 앞으로 가져옴(맨 뒤에 있는 것을 맨 앞으로)
    # 가져올시 순서를 그대로 유지

    for i in range(m):
        if belts[i] is not None:
            length = len(belts[i])

            for j in range(length):
                if belts[i][j][0] == r_id:
                    belt = list(belts[i])

                    front = belt[j:]
                    belt = front + belt

                    belts[i] = deque(belt[:length])


                    print(i + 1)
                    return

    print(-1)


# 벨트고장 함수
def break_belt(command):
    # b_num = 입력 1번째값 - 1
    b_num = command[1] - 1
    # 해당 벨트는 다시 사용할 수 없음
    # 벨트의 바로 오른쪽 벨트부터 순서대로 보며 아직 고장이 나지않은 최초의 벨트 위로 b_num 벨트에 놓여있던 상자들을 아래에서부터 순서대로 하나씩 옮김
    # 단, 모든 벨트가 망가지는 경우는 없음
    # 만약 b_num 벨트가 이미 망가져있다면 -1, 그렇지 않았다면 b_num 값 출력

    if belts[b_num] is None:  # 주의
        print(-1)
    else:

        print(command[1])

        belt_idx = b_num + 1
        for _ in range(m - 1):
            belt_idx = belt_idx % m

            if belts[belt_idx] is not None:  # 주의
                belts[belt_idx] = deque(list(belts[belt_idx]) + list(belts[b_num]))

                # 벨트 고장 표시
                belts[b_num] = None
                return

            belt_idx += 1

# 벨트 리스트 = None
belts = []

# q 입력
q = int(input())
# q만큼 반복하면서
for i in range(q):

    # 명령어 입력받음
    command = list(map(int, input().split()))

    # print("================")
    # print(i, "몇번째", command[0], command[1])

    # 만약 0번째가 100이라면
    if command[0] == 100:
        # 공장설립 함수 호출
        n, m = create_factory(command)
    # elif 200이라면
    elif command[0] == 200:
        # 물건하차 함수 호출
        down_box(command)
    # elif 300이라면
    elif command[0] == 300:
        # 물건제거 함수 호출
        remove_box(command)
    # elif 400이라면
    elif command[0] == 400:
        # 물건확인 함수 호출
        check_box(command)
    # elif 500이라면
    elif command[0] == 500:
        # 벨트고장 함수 호출
        break_belt(command)



