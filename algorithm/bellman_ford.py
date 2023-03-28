import sys
input = sys.stdin.readline
INF = int(1e9)

def bf(start):
  distance[start] = 0

  for i in range(n):
    # 매 반복마다 모든 간선을 확인
    for j in range(m):
      now, next, cost = graph[j]

      if distance[now] != INF and distance[next] > distance[now] + cost:
        distance[next] = distance[now] + cost

        if i == n - 1:
          return True
        
  return False

n, m = map(int, input().split())
graph = []
distance = [INF] * (n + 1)

for _ in range(m):
  a, b, c = map(int, input().split())
  graph.append((a, b, c))

negative_cycle = bf(1)

if negative_cycle:
  print('-1')
else:
  for i in range(2, n + 1):
    if distance[i] == INF:
      print('-1')
    else:
      print(distance[i])