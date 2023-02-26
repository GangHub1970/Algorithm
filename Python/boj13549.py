import heapq

n, k = map(int, input().split())
INF = int(1e9)

distance = [INF] * 100001
distance[n] = 0

def dijstra(start):
  q = []
  heapq.heappush(q, (0, start))

  while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
      continue

    if 0 <= now + 1 and now + 1 < 100001 and distance[now + 1] > dist + 1:
      distance[now + 1] = dist + 1
      heapq.heappush(q, (dist + 1, now + 1))
    if 0 <= now - 1 and now - 1 < 100001 and distance[now - 1] > dist + 1:
      distance[now - 1] = dist + 1
      heapq.heappush(q, (dist + 1, now - 1))
    if 0 <= now * 2 and now * 2 < 100001 and distance[now * 2] > dist:
      distance[now * 2] = dist
      heapq.heappush(q, (dist, now * 2))

dijstra(n)
print(distance[k])