import heapq
import sys
input = sys.stdin.readline
INF = 987654321

v, e = map(int, input().split())

start = int(input())

distance = [INF for _ in range(v+1)]
distance[start] = 0
graph = [[] for _ in range(v + 1)]

for _ in range(e):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

def dijkstra(start):
  q = []
  heapq.heappush(q, [0, start])

  while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
      continue

    for next_node in graph[now]:
      cost = dist + next_node[1]

      if cost < distance[next_node[0]]:
        distance[next_node[0]] = cost
        heapq.heappush(q, [cost, next_node[0]])

dijkstra(start)

for i in range(1, v + 1):
  if distance[i] == INF:
    print("INF")
  else:
    print(distance[i])
