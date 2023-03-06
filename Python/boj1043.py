from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

known_people = list(map(int, input().split()))
if len(known_people) == 1:
  known_people = []
else:
  known_people = known_people[1:]

party = []
graph = [[] for _ in range(n + 1)]
for _ in range(m):
  lst = list(map(int, input().split()))[1:]
  party.append(lst)

  for i in range(len(lst)):
    for j in range(len(lst)):
      if i == j: continue
      graph[lst[i]].append(lst[j])

def bfs(start):
  visited = [False] * (n + 1)
  q = deque()
  q.append(start)
  visited[start] = True
  people.append(start)

  while q:
    now = q.popleft()

    for next in graph[now]:
      if not visited[next]:
        q.append(next)
        people.append(next)
        visited[next] = True

people = []
for p in known_people:
  bfs(p)

count = 0
for p in party:
  result = 0
  for j in p:
    if j in people:
      result = -1
      break
  if result == 0:
    count += 1

print(count)