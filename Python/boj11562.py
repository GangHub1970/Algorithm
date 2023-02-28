import sys
input = sys.stdin.readline

n, m = map(int, input().split())
INF = int(1e9)

distance = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(n + 1):
  distance[i][i] = 0

for _ in range(m):
  a, b, c = map(int, input().split())
  
  distance[a][b] = 0
  if c == 1:
    distance[b][a] = 0
  else:
    distance[b][a] = 1

for bridge in range(1, n + 1):
  for start in range(1, n + 1):
    for end in range(1, n + 1):
      distance[start][end] = min(distance[start][end], distance[start][bridge] + distance[bridge][end])

k = int(input())
for _ in range(k):
  a, b = map(int, input().split())
  print(distance[a][b])
