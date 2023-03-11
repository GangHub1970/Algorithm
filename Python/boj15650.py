n, m = map(int, input().split())

result = []
def f(start):
  if len(result) == m:
    print(' '.join(map(str, result)))
    return
  
  for i in range(start, n + 1):
    result.append(i)
    f(i + 1)
    result.pop()
    
f(1)