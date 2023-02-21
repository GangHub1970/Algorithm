def binary_search(target, start, end):
    if start > end:
        return 0
    
    if target > nums[(start + end) // 2]:
        return binary_search(target, (start + end) // 2 + 1, end)
    elif target < nums[(start + end) // 2]:
        return binary_search(target, start, (start + end) // 2 - 1)
    else:
        return 1

n = int(input())
nums = list(map(int, input().split()))
nums.sort()
m = int(input())
lst = list(map(int, input().split()))

for i in lst:
    if i == lst[-1]:
        print(binary_search(i, 0, n - 1))
    else:
        print(binary_search(i, 0, n - 1), end=' ')