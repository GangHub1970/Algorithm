def get_parent(n):
  if n == SET[n]:
    return n
  
  SET[n] = get_parent(SET[n])
  return SET[n]

def is_set(a, b):
  a = get_parent(a)
  b = get_parent(b)

  if a == b: return True
  return False

def union(a, b):
  a = get_parent(a)
  b = get_parent(b)

  if a < b:
    SET[b] = a
  else:
    SET[a] = b

v, e = map(int, input().split())
graph = []
for _ in range(e):
  graph.append(list(map(int, input().split())))
graph.sort(key = lambda x : x[2])

result = 0
SET = [i for i in range(v)]
for edge in graph:
  a, b, c = edge
  if not is_set(a - 1, b - 1):
    result += c
    union(a - 1, b - 1)

print(result)