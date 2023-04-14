from collections import deque

def bfs():
  q = deque()
  q.append((0, 0))
  count[0][0] = 0

  while q:
    r, c = q.popleft()

    for i in range(4):
      nr = r + dr[i]
      nc = c + dc[i]
      if nr < n and nc < n and nr >= 0 and nc >= 0:
        if count[nr][nc] == -1:
          if rooms[nr][nc] == 1:
            q.appendleft((nr, nc))
            count[nr][nc] = count[r][c]
          else:
            q.append((nr, nc))
            count[nr][nc] = count[r][c] + 1

n = int(input())
rooms = []
for _ in range(n):
  rooms.append(list(map(int, input())))

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
count = [[-1] * n for _ in range(n)]

bfs()
print(count[n - 1][n - 1])