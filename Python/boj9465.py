t = int(input())

for _ in range(t):
  n = int(input())

  board = []
  for _ in range(2):
    board.append(list(map(int, input().split())))
  
  if n == 1:
    print(max(board[0][-1], board[1][-1]))
    continue

  dp = [[0] * n for _ in range(2)]
  for i in range(2):
    dp[i][0] = board[i][0]
  for i in range(2):
    dp[i][1] = dp[(i + 1) % 2][0] + board[i][1]
  
  if n == 2:
    print(max(dp[0][-1], dp[1][-1]))
    continue
  
  for i in range(2, n):
    for j in range(2):
      dp[j][i] = max(dp[(j + 1) % 2][i - 1] + board[j][i], max(dp[j][i - 2], dp[(j + 1) % 2][i - 2] + board[j][i]))
  
  print(max(dp[0][-1], dp[1][-1]))