n = int(input())

rgb = []
for _ in range(n):
    rgb.append(list(map(int, input().split())))

dp = [[0] * 3 for _ in range(n)]
dp[0] = rgb[0]
for i in range(1, n):
    # 각 단계마다 빨강, 초록, 파랑을 뽑았을 때의 최솟값을 dp에 저장
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + rgb[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + rgb[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + rgb[i][2]

print(min(dp[n - 1]))