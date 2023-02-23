n = int(input())
quantity = []
for _ in range(n):
    quantity.append(int(input()))

dp = [0] * n
dp[0] = quantity[0]
if n >= 2:
    dp[1] = dp[0] + quantity[1]
if n >= 3:
    dp[2] = max(dp[1], quantity[0] + quantity[2], quantity[1] + quantity[2])
if n >= 4:
    for i in range(3, n):
        jump = dp[i - 2] + quantity[i]
        next = dp[i - 3] + quantity[i - 1] + quantity[i]
        dp[i] = max(dp[i - 1], jump, next)

print(dp[-1])