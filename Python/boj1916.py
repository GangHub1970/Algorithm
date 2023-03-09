import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
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

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

start, end = map(int, input().split())
distance = [INF] * (n + 1)

dijkstra(start)
print(distance[end])