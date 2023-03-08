import sys
a, b, c = map(int, sys.stdin.readline().split())

def f(n):
  if n == 1:
    return a % c
  
  tmp = f(n // 2)
  if n % 2 == 0:
    return (tmp * tmp) % c
  else:
    return (tmp * tmp * a) % c
  
print(f(b))