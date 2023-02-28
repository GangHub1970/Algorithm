def get_parent(n):
  if n == parent[n]:
    return n

  parent[n] = get_parent(parent[n])
  return parent[n]

def is_set(a, b):
  a = get_parent(a)
  b = get_parent(b)

  if a == b:
    return True
  return False

def union(a, b):
  a = get_parent(a)
  b = get_parent(b)

  if a < b:
    parent[b] = a
  else:
    parent[a] = b

def is_cross(a, b):
  if school[a] != school[b]:
    return True
  return False

n, m = map(int, input().split())
school = input().split()
graph = []
for _ in range(m):
  graph.append(list(map(int, input().split())))
graph.sort(key = lambda x : x[2])

result = 0
count = 0
parent = [i for i in range(n + 1)]
for edge in graph:
  a, b, c = edge

  if not is_set(a, b) and is_cross(a - 1, b - 1):
    result += c
    count += 1
    union(a, b)

if count != n - 1:
  print(-1)
else:
  print(result)