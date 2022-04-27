# 문제이해: 9:20 ~ 9:46
# 풀이: 9:46 ~ 11:20(f)

# 현재 설치된 구조물이 규칙에 맞는지 확인하는 함수
def possible(answer):
    # answer 2차원 배열이 그림과 위아래가 거꾸로 이기 때문에, 기둥은 밑(0(위)->아래)로 올라감
    for x, y, stuff in answer:
        # 기둥인 경우
        if stuff == 0:
            # 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있는 경우
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False
        # 보인 경우
        elif stuff == 1:
            # 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야함
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False

    return True


def solution(n, build_frame):
    answer = []

    # for - 설치 작업을 반복하면서:
    for frame in build_frame:
        # x : 구조물 위치
        # y : 구조물 위치
        # stuff : 설치 구조물 - 기둥(0), 보(1)
        # operate : 행동 종류 - 삭제(0), 설치(1)
        x, y, stuff, operate = frame

        # 만약 삭제인 경우
        if operate == 0:
            # 일단 삭제하고
            answer.remove([x, y, stuff])
            # 규칙에 맞는 구조물인지 확인
            if not possible(answer):
                # 가능한 구조물이 아니라면 다시 설치
                answer.append([x, y, stuff])

        # 만약 설치인 경우
        if operate == 1:
            # 일단 설치하고
            answer.append([x, y, stuff])
            # 규칙에 맞는 구조물인지 확인
            if not possible(answer):
                # 가능한 구조물이 아니라면 다시 설치
                answer.remove([x, y, stuff])

    return sorted(answer) # x 기준으로 정렬된 결과를 반환

#입력
# n : 설치 벽 크기
# build_frame : 설치 작업(설치 구조물 x좌표, 설치 구조물 y좌표, 설치구조물, 행동 종류)
n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
print(solution(n, build_frame))