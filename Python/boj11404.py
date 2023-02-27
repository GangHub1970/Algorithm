import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
distance = [[INF] * n for _ in range(n)]

for _ in range(m):
  a, b, c = map(int, input().split())
  distance[a - 1][b - 1] = min(distance[a - 1][b - 1], c)

for bridge in range(n):
  for start in range(n):
    for end in range(n):
      if start == end:
        distance[start][end] = 0
        continue

      distance[start][end] = min(distance[start][end], distance[start][bridge] + distance[bridge][end])

for i in distance:
  for j in i:
    if j == INF:
      print(0, end=' ')
    else:
      print(j, end=' ')
  print()
    