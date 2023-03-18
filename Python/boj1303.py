from collections import deque

m, n = map(int, input().split())
board = []
for _ in range(n):
  board.append(list(input()))
  
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(a, b):
  q = deque()
  q.append((a, b))
  now = board[a][b]
  count = 1
  board[a][b] = 0

  while q:
    r, c = q.popleft()

    for i in range(4):
      if r + dr[i] < n and c + dc[i] < m and r + dr[i] >= 0 and c + dc[i] >= 0:
        nr = r + dr[i]
        nc = c + dc[i]
        if board[nr][nc] == now:
          count += 1
          board[nr][nc] = 0
          q.append((nr, nc))

  return count

w = 0
b = 0
for i in range(n):
  for j in range(m):
    if board[i][j] == 'W':
      c = bfs(i, j)
      w += c ** 2
    elif board[i][j] == 'B':
      c = bfs(i, j)
      b += c ** 2
print(w, b)
      
