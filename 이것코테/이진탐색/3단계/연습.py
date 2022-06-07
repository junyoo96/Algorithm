n, c = map(int, input().split())

houses = []
for _ in range(n):
    houses.append(int(input()))
houses.sort()

start = houses[1] - houses[0]
end = houses[-1] - houses[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    count = 1
    value = houses[0]

    for i in range(1, n):
        if houses[i] >= value + mid:
            value = houses[i]
            count += 1
    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)
