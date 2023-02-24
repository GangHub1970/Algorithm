import heapq
INF = int(1e9)

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))

  while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
      continue

    for next in graph[now]:
      cost = dist + next[1]

      if distance[next[0]] > cost:
        distance[next[0]] = cost
        heapq.heappush(q, (cost, next[0]))

n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
  a, b, c = map(int, input().split())

  graph[a].append((b, c))

count = []
for i in range(1, n + 1):
  distance = [INF] * (n + 1)
  distance[i] = 0
  distance[0] = -1

  dijkstra(i)
  count.append(distance)

result = []
for i in range(n):
  result.append(count[i][x] + count[x - 1][i + 1])

print(max(result))
