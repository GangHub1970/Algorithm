from collections import deque

def bfs(r, c):
  q = deque()
  q.append((r, c))
  distance[r][c] = 0
  fish = []

  while q:
    row, col = q.popleft()

    for i in range(4):
      if row + dr[i] >= 0 and col + dc[i] >= 0 and row + dr[i] < n and col + dc[i] < n:
        nr = row + dr[i]
        nc = col + dc[i]
        if state[nr][nc] <= shark and distance[nr][nc] == -1:
          q.append((nr, nc))
          distance[nr][nc] = distance[row][col] + 1
          if state[nr][nc] != 0 and state[nr][nc] < shark:
            fish.append([nr, nc, distance[nr][nc]])

  return fish

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

n = int(input())

state = []
for _ in range(n):
  state.append(list(map(int, input().split())))

shark = 2
dist = 0
count = 0
x, y = 0, 0

for i in range(n):
  for j in range(n):
    if state[i][j] == 9:
      state[i][j] = 0
      x, y = i, j
      break

while True:
  distance = [[-1] * n for _ in range(n)]
  fish = bfs(x, y)

  if fish == []: break
  fish.sort(key = lambda x : (x[2], x[0], x[1]))

  dist += fish[0][2]
  state[fish[0][0]][fish[0][1]] = 0
  count += 1
  if count == shark:
    shark += 1
    count = 0

  x, y = fish[0][0], fish[0][1]

print(dist)