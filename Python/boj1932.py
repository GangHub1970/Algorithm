n = int(input())
triangle = []
for _ in range(n):
  triangle.append(list(map(int, input().split())))

dp = []
for i in range(n):
  dp.append([0] * (i + 1))
dp[0][0] = triangle[0][0]

for i in range(1, n):
  for j in range(i + 1):
    if j == 0:
      dp[i][0] = dp[i - 1][0] + triangle[i][0]
      continue
    if j == i:
      dp[i][i] = dp[i - 1][i - 1] + triangle[i][i]
      continue
    for h in range(j - 1, j + 1):
      dp[i][j] = max(dp[i][j], dp[i - 1][h] + triangle[i][j])

print(max(dp[-1]))