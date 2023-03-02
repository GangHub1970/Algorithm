import sys
from collections import deque
input = sys.stdin.readline

MAX = 10_000

def D(n):
  return (2 * n) % 10000

def S(n):
  if n == 0:
    return 9999
  return n - 1

def L(n):
  return 10 * (n % 1000) + n // 1000

def R(n):
  return 1000 * (n % 10) + n // 10

def bfs():
  q = deque()
  q.append((a, ''))
  visited[a] = True

  while q:
    now, result = q.popleft()
    if now == b:
      return result

    for next in [(D(now), 'D'), (S(now), 'S'), (L(now), 'L'), (R(now), 'R')]:
      if not visited[next[0]]:
        q.append((next[0], result + next[1]))
        visited[next[0]] = True

t = int(input())
for _ in range(t):
  a, b = map(int, input().split())
  
  visited = [False] * MAX
  print(bfs())
  