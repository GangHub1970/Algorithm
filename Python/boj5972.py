import heapq
INF = int(1e9)

def dijkstra():
  q = []
  heapq.heappush(q, (0, 1))

  while q:
    cost, now = heapq.heappop(q)

    if count[now] < cost:
      continue
    
    for next in graph[now]:
      next_cost = cost + next[1]

      if count[next[0]] > next_cost:
        count[next[0]] = next_cost
        heapq.heappush(q, (next_cost, next[0]))

n, m = map(int, input().split())
count = [INF for _ in range(n + 1)]
count[1] = 0

graph = [[] for _ in range(n + 1)]
for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))

dijkstra()
print(count[n])