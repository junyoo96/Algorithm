# 10:58~11:30/11:30~ - 틀림(순열조합 문제인줄 알고 dfs 사용했다가 시간초과)

# n : 단어 개수
# 단어
# 알파벳 대문자로만 이루어짐
# 알파벳 대문자를 0~9까지의 숫자 중 하나로 바꾸어 N개의 수를 합하는 문제
# 같은 알파벳은 같은 숫자로 바꾸고, 두개 이상의 알파벳이 같은 숫자로 바뀌면 안됨

# 모든 단어에 포함되어 있는 알파벳은 최대 10개
# 수의 최대길이는 8개

# answer : n개의 단어가 주어졌을 때, 수의 합 최대 구하기
# 0~9 중 주어진 알파벳 개수만큼 숫자를 뽑는다고 생각하기
# 그리디로 해결
# ============================================
from collections import defaultdict

n = int(input())
# 단어를 저장할 리스트
words = []
for _ in range(n):
    words.append(input().rstrip())

# 단어 내의 알파벳별로 가중치 수를 저장하는 변수
dictionary = defaultdict(lambda: 0)
for word in words:
    for i in range(len(word)):
        # 알파벳에 위치한 자릿수에 맞게 가중치 수 더하기
        dictionary[word[i]] += 10 ** (len(word) - i - 1)

# 알파벳 별 가중치 수 저장할 변수
array = list(dictionary.values())
# 가중치 수가 큰것부터 나오게 내림차순 정렬
array.sort(reverse=True)

answer = 0
# 해당 알파벳에 어떤 숫자를 지정할지(0~9까지 가능),
num = 9
for i in range(len(array)):
    # 가장 큰 가중치 수 부터 가장 큰 숫자인 9를 지정
    answer += array[i] * num
    # 다음 작은 숫자로 이동
    num -= 1

print(answer)