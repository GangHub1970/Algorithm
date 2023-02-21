n = int(input())
arr_n = list(map(int, input().split()))

dp = [0] * n
dp[0] = arr_n[0]
for i in range(1, n):
    dp[i] = max(dp[i - 1] + arr_n[i], arr_n[i])

print(max(dp))