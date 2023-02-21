def lower(target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if target > nums[mid]:
            start = mid + 1
        else:
            end = mid - 1
            
    return start


def upper(target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if target >= nums[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return start

        

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