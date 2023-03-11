n, m = map(int, input().split())

result = []
def f(start):
  if len(result) == m:
    print(' '.join(map(str, result)))
    return
  
  for i in range(start - 1, n + 1):
    if i == 0: continue
    result.append(i)
    f(i + 1)
    result.pop()

f(1)