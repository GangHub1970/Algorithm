n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

result = []
def f():
  if len(result) == m:
    print(' '.join(map(str, result)))
    return
  
  for i in range(n):
    if nums[i] not in result:
      result.append(nums[i])
      f()
      result.pop()

f()
