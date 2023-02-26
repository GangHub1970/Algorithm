n = int(input())

dp = [[0 for _ in range(10)] for _ in range(100)]

dp[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for i in range(1, 100):
  for j in range(10):
    if j == 0:
      dp[i][j] = dp[i - 1][j + 1]
      continue
    if j == 9:
      dp[i][j] = dp[i - 1][j - 1]
      continue
    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

print(sum(dp[n - 1]) % 1_000_000_000)