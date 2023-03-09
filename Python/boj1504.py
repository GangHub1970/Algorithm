import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start, end):
  q = []
  heapq.heappush(q, (0, start))
  distance = [INF] * (n + 1)
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
      continue
    
    for next_node, d in graph[now]:
      cost = dist + d
      if cost < distance[next_node]:
        distance[next_node] = cost
        heapq.heappush(q, (cost, next_node))
  
  return distance[end]

n, e = map(int, input().split())

graph =[[] for _ in range(n + 1)]
for _ in range(e):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))

nodes = list(map(int, input().split()))

result = []
for i in range(2):
  first = dijkstra(1, nodes[i])
  second = dijkstra(nodes[i], nodes[1 - i])
  third = dijkstra(nodes[1 - i], -1)

  result.append(first + second + third)

if min(result) >= INF:
  print(-1)
else:
  print(min(result))