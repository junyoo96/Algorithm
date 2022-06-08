#1:46~

# 이진 탐색 라이브러리
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    # a라는 정렬된 배열에 right_value(query값) 삽입할 때 삽입할 원소가 위치할 인덱스
    right_index = bisect_right(a, right_value)
    # a라는 정렬된 배열에 right_value(query값) 삽입할 때 삽입할 원소가 위치할 인덱스
    left_index = bisect_left(a, left_value)

    # ? 쿼리에 해당하는 데이터 개수 구하기
    return right_index - left_index

# 모든 단어를 길이마다 나누어서 저장하기 위한 리스트
    # 0부분은 안쓰고 1~10000 사용
array = [[] for _ in range(10001)]
# 모든 단어를 길이마다 나누어서 뒤집어 저장하기 위한 리스트
reversed_array = [[] for _ in range(10001)]

# words : 쿼리로 매치할 전체 단어 리스트
# queries : 쿼리 키워드 리스트
def solution(words, queries):
    answer = [] # 각 쿼리별로 매치된 단어의 개수 리스트
    # 모든 단어를 접미사 와일카드 배열, 접두사 와일드카드 배열에 각각 삽입
    for word in words:
        # 단어 길이에 따라 단어 삽입
        array[len(word)].append(word)
        # 단어 길이에 따라 뒤집은 단어를 삽입(??aa 이런 단어 때문)
        reversed_array[len(word)].append(word[::-1])

    # 이진 탐색을 수행하기 위해 각 단어 리스트 정렬 수행
    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()

    # 각 쿼리를 반복하면서
    for q in queries:
        # 접미사에 와일드카드가 붙은 경우
        if q[0] != '?':
            # ex) fro??이면 froaa~frozz사이에 해당하는 모든 원소 개수를 계산하기
            res = count_by_range(array[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
        else:
            # ex) ??fro이면 aafro~zzfro사이에 해당하는 모든 원소 개수를 계산하기
            res = count_by_range(reversed_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?','z'))

        # 검색된 단어의 개수 저장
        answer.append(res)

    return answer