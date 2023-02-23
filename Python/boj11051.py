n, k = map(int, input().split())

dp = [0] * 1001
dp[0] = 1
dp[1] = 1
for i in range(2, 1001):
    dp[i] = dp[i - 1] * i

result = dp[n] // (dp[n - k] * dp[k])
print(result % 10007)