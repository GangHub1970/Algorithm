n, m = map(int, input().split())

board = []
for _ in range(n):
  board.append(list(input()))

result = []
for i in range(n - 7):
  for j in range(m - 7):
    lst = []
    for kind in ['W', 'B']:
      start = (i + j) % 2
      count = 0
      for h in range(i, i + 8):
        for k in range(j, j + 8):
          if (h + k) % 2 == start and board[h][k] != kind:
            count += 1
          elif (h + k) % 2 != start and board[h][k] == kind:
            count += 1
      lst.append(count)
    result.append(min(lst))

print(min(result))