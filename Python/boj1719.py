import heapq
INF = int(1e9)

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))

  while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
      continue

    for next_node, next_dist in graph[now]:
      cost = dist + next_dist

      if cost < distance[next_node]:
        distance[next_node] = cost
        route[next_node] = (now, next_node)
        heapq.heappush(q, (cost, next_node))

def get_route(target, start):
  if route[start][0] == target:
    return route[start][1]

  return get_route(target, route[start][0])

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))

result = [['-' for _ in range(n)] for _ in range(n)]
best_route = [[] for _ in range(n)]
for i in range(1, n + 1):
  distance = [INF] * (n + 1)
  route = [0 for _ in range(n + 1)]
  dijkstra(i)
  
  for j in range(1, n + 1):
    if i == j:
      best_route[i - 1].append('-')
      continue

    best_route[i - 1].append(get_route(i, j))

for i in best_route:
  print(*i)