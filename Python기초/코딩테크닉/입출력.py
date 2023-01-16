# 입력관련

# 붙어있는 문자열(숫자로 된 문자열도 동일) 입력받기
'''
입력 문자열
RRRBB
GGBBB
'''
graph = []
print(graph)
#[['R', 'R', 'R', 'B', 'B'], ['G', 'G', 'B', 'B', 'B']]

# 입력개수가 주어지지 않은 입력 받기
"""
입력 문자열
Hello
Baekjoon
Online Judge
"""


# 끊어서 입력받기(10개씩)- 틀림 X
"""
입력문자열
aaaaaaaaaabbbbbbbbbb
"""

# split() 과 split(" ")의 차이
string = "word1 word2  word3    word4     "

# ['word1', 'word2', 'word3', 'word4']

# ['word1', 'word2', '', 'word3', '', '', 'word4', '', '', '', '']

#================================================================
# 출력관련

# 개행없이 출력