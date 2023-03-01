import sys
input = sys.stdin.readline

def get_parent(n):
  if n == parent[n]:
    return n
  
  parent[n] = get_parent(parent[n])
  return parent[n]

def is_set(a, b):
  a = get_parent(a)
  b = get_parent(b)

  if a == b: return True
  return False

def union(a, b):
  a = get_parent(a)
  b = get_parent(b)

  if a in power and b not in power:
    parent[b] = a
  elif a not in power and b in power:
    parent[a] = b
  else:
    if a < b:
      parent[b] = a
    else:
      parent[a] = b

n, m, k = map(int, input().split())
power = list(map(int, input().split()))

graph = []
for _ in range(m):
  graph.append(list(map(int, input().split())))
graph.sort(key = lambda x : x[2])

result = 0
parent = [i for i in range(n + 1)]

for edge in graph:
  a, b, c = edge

  if not is_set(a, b):
    if get_parent(a) in power and get_parent(b) in power: continue

    result += c
    union(a, b)

print(result)