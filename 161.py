dp = []
for i in range(40):
    dp.append([-1, -1])

dp[1] = [1, 1]

def count(length, end):
    if dp[length][end] != -1:
        return dp[length][end]
    if length == 1:
        dp[length][end] = 1
        return 1
    if end == 0:
        dp[length][end] = count(length - 1 , 0) + count(length - 1, 1)
    else:
        dp[length][end] = count(length - 1, 0)
    return dp[length][end]

print(count(35, 0), count(35, 1))

print(sum(dp[30]))
# print(dp)

# ANSWER must be less than 30 but very close to 30. so try for 29, 28, 27, etc

# ANSWER IS 28.