INF = int(1e9)

n, m = map(int, input())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a][b] = c

for i in range(1, n + 1):
  graph[i][i] = 0

for bridge in range(1, n + 1):
  for start in range(1, n + 1):
    for end in range(1, n + 1):
      graph[start][end] = min(graph[start][end], graph[start][bridge] + graph[bridge][end])

for i in range(1, n + 1):
  for j in range(1, n + 1):
    if graph[i][j] == INF:
      print('INFINITY', end=' ')
    else:
      print(graph[i][j], end=' ')
  print()