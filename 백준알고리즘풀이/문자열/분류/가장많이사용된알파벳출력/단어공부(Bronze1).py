string = input()
counts = [0] * 26
for s in string:
    counts[ord(s.lower()) - ord('a')] += 1

max_value = max(counts)
if counts.count(max_value) == 1:
    print(chr(counts.index(max_value)+ord('A')))
else:
    print("?")