import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(distance, node):
  q = []
  heapq.heappush(q, (0, 1))

  while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
      continue

    for next in graph[now]:
      if node == (now, next[0]) or node == (next[0], now):
        continue

      cost = dist + next[1]

      if cost < distance[next[0]]:
        distance[next[0]] = cost
        route[next[0]] = (now, next[0])
        heapq.heappush(q, (cost, next[0]))

def get_route(n):
  if n == 1:
    return
  
  best_route.append(route[n])
  get_route(route[n][0])

n, m = map(int, input().split())
distance = [INF] * (n + 1)
distance[1] = 0 
graph = [[] for _ in range(n + 1)]
route = [0] * (n + 1)

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))

dijkstra(distance, (0, 0))
best_route = []
get_route(n)

result = []
for node in best_route:
  distance_delay = [INF] * (n + 1)
  distance_delay[1] = 0

  dijkstra(distance_delay, node)
  if distance_delay[n] == INF:
    result.append(INF)
    continue

  result.append(distance_delay[n] - distance[n])

count = max(result)
if count == INF:
  print(-1)
else:
  print(count)