SET = [i for i in range(10)]

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

edges = [[1, 2, 10], [2, 3, 20], [3, 1, 5]]
edges.sort(key = lambda x : x[2])

ans = 0
for edge in edges:
  a, b, c = edge
  if not is_set(a, b):
    ans += c
    union(a, b)

print(ans)