def solution(game_board, table):

    # game_board의 빈칸, table의 블럭 찾는 함수
    # mat : 어떤 행열에서(게임보드 or 테이블) 찾을지
    # num : 어떤 값을 찾을지
    def finding(matrix, num):
        # return할 블럭 및 빈칸들이 들어있는 배열
        arr = []
        # 방문 여부
        visit = [[0] * n for _ in range(n)]
        # 행열을 탐색하면서
        for i in range(n):
            for j in range(n):
                # 만약 현재 찾는 것(블럭 / 빈칸)과 같고 방문하지 않았으면 BFS
                if matrix[i][j] != num or visit[i][j]:
                    continue

                # bfs 시작
                queue = [[i, j]]
                # 현재 좌표 방문처리
                visit[i][j] = 1
                # 한 퍼즐당 차지하는 칸의 개수 변수
                k = 0
                # 현재 queue의 길이가 퍼즐의 현재 칸의 개수보다 작은동안 반복하면서
                while k < len(queue):
                    r, c = queue[k]
                    # 상하좌우를 반복하면서
                    for d in range(4):
                        nr, nc = r + dr[d], c + dc[d]
                        # 만약 이동할 좌표가 올바른 범위안에 있다면
                        if 0 <= nr < n and 0 <= nc < n:
                            # 만약 이동할 좌표를 방문한적이 없고 이동할좌표가 찾고자 하는 값이라면
                            if not visit[nr][nc] and matrix[nr][nc] == num:
                                # queue에 이동할 좌표 넣고 방문처리
                                queue.append([nr, nc])
                                visit[nr][nc] = 1

                    # 한 퍼즐당 차지하는 칸의 개수 카운트
                    k += 1

                # 도형(빈칸 or 블럭)의 좌표 추가
                arr.append(queue)

        return arr

    # 중요 - 도형 하나(빈칸 or 블록)의 좌표들을 1개의 문자열로 이어서 반환
    def hashing(group):
        # 해당 도형 위치의 가장 왼쪽 모서리 값
        min_r, min_c = 50, 50 # 가로,세로 크기가 50이 가장 최대이므로 50으로 두고 시작
        # 도형의 좌표들을 반복하면서 가장 왼쪽 모서리 값 찾기
        for r, c in group:
            min_r = min(min_r, r)
            min_c = min(min_c, c)

        # 중요 - 도형의 좌표들을 도형을 왼쪽 구석에 넣었을때 위치로 갱신
        for i in range(len(group)):
            group[i][0] -= min_r
            group[i][1] -= min_c

        # 중요 - 최선 행, 차선 열 오름차순으로 정렬 - 나중에 블록과 빈칸이 서로 맞는지 비교할 때 문자열화된 좌표로 비교할 것이므로 정렬을 함으로서, 순서가 다르더라도 같은 좌표들 구성이면 같은 영역임을 확인하기 위함
        group.sort()

        # 중요 - 도형의 좌표를 문자열로 바꿔주고 return
        arr = []
        for r, c in group:
            arr.append(str(r))
            arr.append(str(c))

        return ''.join(arr)

    # 중요 - 빈칸의 위치를 90도 회전시키는 함수
    def rotate(shape):
        for i in range(len(shape)):
            r, c = shape[i]
            shape[i] = [c, -r]

    # 게임보드의 길이
    n = len(game_board)
    # 방향 리스트
    dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
    # 채울 수 있는 최대 칸수
    answer = 0

    # 블럭(조각)과 빈칸의 좌표 찾기
    block = finding(table, 1) # 테이블에서 블럭(1) 찾기
    blank = finding(game_board, 0) # 게임보드에서 빈칸(0) 찾기

    # 각 블러들의 좌표를 문자열로 해싱후 딕셔너리에 저장
    for i in range(len(block)):
        block[i] = hashing(block[i])

    # 블럭을 반복하면서
    temp = dict()
    for i in block:
        # key : 각 블럭의 문자열로 된 좌표들 value: 해당 블럭의 개수
        temp[i] = temp.get(i, 0) + 1
    block = temp

    # 빈칸들을 반복하면서
    for i in range(len(blank)):
        # 해당 빈칸을 4번 90도 회전하며, 맞는 블럭이 있는지 탐색
        for _ in range(4):
            # 현재 블럭을 회전
            rotate(blank[i])
            # 현재 빈칸의 좌표들을 문자열로 변환
            hash_blank = hashing(blank[i])
            # 만약 현재 블럭과 알맞은 빈칸이 있으면(블럭과 빈칸의 문자열이 같다면)
            if block.get(hash_blank):
                # 블럭을 사용했으므로 딕셔너리에서 개수 -1
                block[hash_blank] -= 1

                # 인덱스가 행열행열....식으로 들어가기 때문에, 문자열의 길이 //2 가 해당 블록의 칸의 개수가 되므로 answer에 추가
                answer += len(hash_blank)//2
                break

    return answer

if __name__ == '__main__':
    game_board = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
    table = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]
    print(solution(game_board, table))