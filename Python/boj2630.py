def cut(n, x, y):
  now = paper[x][y]
  if n == 1:
    result.append(now)
    return

  count = 0
  for i in range(n):
    for j in range(n):
      if paper[x + i][y + j] != now:
        count += 1
        break
    if count > 0: break
  
  if count > 0:
    cut(n // 2, x, y)
    cut(n // 2, x + n // 2, y)
    cut(n // 2, x, y + n // 2)
    cut(n // 2, x + n // 2, y + n // 2)
  else:
    result.append(now)

n = int(input())
paper = []
for _ in range(n):
  paper.append(list(map(int, input().split())))

result = []
cut(n, 0, 0)
print(result.count(0))
print(result.count(1))