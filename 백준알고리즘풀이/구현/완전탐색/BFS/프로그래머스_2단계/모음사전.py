# 12:37~12:42/12:42~12:45
from itertools import product

def solution(word):
    answer = 0

    dictionary = []
    for i in range(1, 6):
        for w in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            dictionary.append(''.join(list(w)))

    dictionary.sort()
    answer = dictionary.index(word) + 1

    return answer