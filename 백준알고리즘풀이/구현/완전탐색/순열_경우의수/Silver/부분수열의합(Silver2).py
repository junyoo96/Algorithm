def dfs(idx, num_sum):
    global answer

    if idx != 0 and num_sum == s:
        answer += 1

    for i in range(idx, n):
        st.append(nums[i])
        dfs(i + 1, num_sum + nums[i])
        st.pop()

n, s = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
st = []
answer = 0

dfs(0, 0)
print(answer)