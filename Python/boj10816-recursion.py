def lower(target, start, end):
    if start > end:
        return start

    mid = (start + end) // 2
    if target > nums[mid]:
        return lower(target, mid + 1, end)
    else:
        return lower(target, start, mid - 1)

def upper(target, start, end):
    if start > end:
        return start

    mid = (start + end) // 2
    if target >= nums[mid]:
        return upper(target, mid + 1, end)
    else:
        return upper(target, start, mid - 1)

        

n = int(input())
nums = list(map(int, input().split()))
nums.sort()
m = int(input())
cards = list(map(int, input().split()))

for card in cards:
    if card == cards[-1]:
        print(upper(card, 0, n - 1) - lower(card, 0, n - 1))
    else:
        print(upper(card, 0, n - 1) - lower(card, 0, n - 1), end=' ')