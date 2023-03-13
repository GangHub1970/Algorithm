from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

visited = [False] * (n + 1)
parent = [[] for _ in range(n + 1)]

def bfs():
  q = deque()
  q.append(1)
  visited[1] = True

  while q:
    now = q.popleft()

    for next in graph[now]:
      if not visited[next]:
        q.append(next)
        parent[next].append(now)
        visited[next] = True

bfs()
for i in range(2, n + 1):
  print(parent[i][0])