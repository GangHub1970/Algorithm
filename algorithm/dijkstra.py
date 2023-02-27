import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
  a, b, c = map(int, input().split())
  # a 노드에서 b 노드로 가는 비용이 c
  graph[a].append((b, c))

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)

    # 현재 노드까지 가는 거리가 더 적은경우는 건너뛴다.
    if distance[now] < dist:
      continue

    for i in graph[now]:
      cost = dist + i[1]

      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra(start)
for i in range(1, n + 1):
  # 도달할 수 없는 경우 INFINITY라고 출력
  if distance[i] == INF:
    print('INFINITY')
  else:
    print(distance[i])