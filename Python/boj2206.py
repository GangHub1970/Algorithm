from collections import deque

def bfs():
  q = deque()
  q.append((0, 0, 0))
  visited[0][0][0] = 1

  while q:
    r, c, b = q.popleft()
    if r == n - 1 and c == m - 1:
      return visited[r][c][b]

    for i in range(4):
      if r + dr[i] < n and c + dc[i] < m and r + dr[i] >= 0 and c + dc[i] >= 0:
        nr = r + dr[i]
        nc = c + dc[i]
        if visited[nr][nc][b] != 0: continue

        if graph[nr][nc] == 1 and b == 0:
          q.append((nr, nc, 1))
          visited[nr][nc][1] = visited[r][c][0] + 1

        if graph[nr][nc] == 0:
          q.append((nr, nc, b))
          visited[nr][nc][b] = visited[r][c][b] + 1
        
n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, list(input()))))

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

result = bfs()
if result == None:
  print(-1)
else:
  print(result)