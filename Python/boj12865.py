n, k = map(int, input().split())

dp = [[0] * (k + 1) for _ in range(n + 1)]
items = [[0, 0]]
for _ in range(n):
  items.append(list(map(int, input().split())))

for i in range(1, n + 1):
  for j in range(1, k + 1):
    w, p = items[i]

    if j < w:
      dp[i][j] = dp[i - 1][j]
    else:
      dp[i][j] = max(p + dp[i - 1][j -  w], dp[i - 1][j])

print(dp[n][k])
