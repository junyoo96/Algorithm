# 1:29~2:00 / 2:00~2:12

# 장르별로 가장 많이 재생된 노래 2개씩
# 장르에 속한 곡이 하나면, 하나만 선택
# 노래
    # 고유 번호로 구분
# 수록기준
    # 속한 노래가 많이 재생된 장르 먼저 수록
    # 장르 내에서 많이 재생된 노래 먼저 수록
    # 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래 먼저 수록
# genre : 노래 장르(1~10000)
# 장르 종류(1~99)
# plays : 노래 재생 횟수(1~10000)
# answer : 베스트 앨범에 들어간 노래의 고유 번호 순서대로 반환
# =================================================
from collections import defaultdict

def solution(genres, plays):
    answer = []

    # 곡 개수 구하기
    length = len(genres)
    # 장르별 총 플레이횟수 개수 dictionary
    play_count = defaultdict(lambda: 0)
    # 장르별 곡 정보들(곡 번호, 곡 재생 횟수) dictinary
    song_info = defaultdict(lambda: [])
    # 곡 개수 만큼 반복하면서
    for i in range(length): # O(N)
        # 해당 장르가 몇번 재생됐는지 저장
        play_count[genres[i]] += plays[i]
        # 곡 정보 저장
        song_info[genres[i]].append((i, plays[i]))

    # 장르별 곡 정보를 반복하면서
    for genre, info in song_info.items(): # O(장르개수)
        # 재생횟수로 기준으로 내림차순 정렬, 고유 번호기준 오름차순 정렬해서 원래 리스트를 정렬한 리스트로 갱신
        song_info[genre] = sorted(info, key=lambda x: (-x[1], x[0])) # O(NlogN)

    # 장르들을 노래 재생 횟수기준으로 내림차순 정렬 # O(NlogN)
    new_play_count = sorted(play_count.items(), key=lambda x: -x[1])

    # 정렬한 장르들을 반복하면서
    for genre, _ in new_play_count: # O(장르개수)
        # 현재 장르에 해당하는 곡들 중 2개를 가져와서 인덱스를 answer에 추가(슬라이싱)
        answer.extend([x[0] for x in song_info[genre][:2]])

    return answer