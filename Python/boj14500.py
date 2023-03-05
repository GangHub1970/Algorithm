import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
for _ in range(n):
  board.append(list(map(int, input().split())))

result = []
for i in range(n):
  for j in range(m):
    count = 0
    if j + 3 < m:
      count = max(count, sum(board[i][j:j + 4]))
    if i + 3 < n:
      s = 0
      for h in range(4):
        s += board[i + h][j]
      count = max(count, s)

    if i + 1 < n and j + 1 < m:
      count = max(count, sum(board[i][j:j + 2]) + sum(board[i + 1][j:j + 2]))
    
    shapes = [
      [(0, 0), (0, 1), (0, 2), (1, 2)],
      [(0, 0), (0, 1), (0, 2), (-1, 2)],
      [(0, 0), (1, 0), (2, 0), (2, 1)],
      [(0, 0), (1, 0), (2, 0), (2, -1)]
    ]
    d = [1, -1]
    for shape in shapes:
      for h in range(2):
        if i + shape[-1][0] * d[h] < n and i + shape[-1][0] * d[h] >= 0 and j + shape[-1][1] * d[h] < m and j + shape[-1][1] * d[h] >= 0:
          s = 0
          for k in shape:
            s += board[i + k[0] * d[h]][j + k[1] * d[h]]
          count = max(count, s)
    
    shapes = [
      [(0, 0), (1, 0), (1, 1), (2, 1)],
      [(0, 0), (1, 0), (1, -1), (2, -1)],
      [(0, 0), (0, 1), (-1, 1), (-1, 2)],
      [(0, 0), (0, 1), (1, 1), (1, 2)]
    ]
    for shape in shapes:
      for h in range(2):
        if i + shape[-1][0] * d[h] < n and i + shape[-1][0] * d[h] >= 0 and j + shape[-1][1] * d[h] < m and j + shape[-1][1] * d[h] >= 0:
          s = 0
          for k in shape:
            s += board[i + k[0] * d[h]][j + k[1] * d[h]]
          count = max(count, s)

    shapes = [
      [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2)],
      [(0, 0), (0, -1), (0, -2), (1, -1), (1, -2)],
      [(0, 0), (1, 0), (2, 0), (1, -1), (2, -1)],
      [(0, 0), (1, 0), (2, 0), (1, 1), (2, 1)]
    ]
    for shape in shapes:
      for h in range(2):
        if i + shape[-1][0] * d[h] < n and i + shape[-1][0] * d[h] >= 0 and j + shape[-1][1] * d[h] < m and j + shape[-1][1] * d[h] >= 0:
          s = 0
          for k in range(4):
            s += board[i + shape[k][0] * d[h]][j + shape[k][1] * d[h]]
          count = max(count, s)
    result.append(count)

print(max(result))