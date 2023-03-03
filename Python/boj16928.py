from collections import deque

def bfs():
  q = deque()
  q.append(0)
  visited[0] = True

  while q:
    now = q.popleft()

    for i in range(6, 0, -1):
      next = now + i

      if next >= 100: continue

      if state[next] != -1:
        next = state[next]

      if not visited[next]:
        visited[next] = True
        distance[next] = distance[now] + 1
        q.append(next)

n, m = map(int, input().split())
state = [-1] * 100

for _ in range(n + m):
  a, b = map(int, input().split())
  state[a - 1] = b - 1

distance = [0] * 100
visited = [False] * 100

bfs()
print(distance[-1])