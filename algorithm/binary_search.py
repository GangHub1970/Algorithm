# 이진 탐색
# 정렬된 상태에서 사용
def binary_search(target, arr, start, end):
  while start <= end:
    mid = (start + end) // 2

    if target > arr[mid]:
      start = mid + 1
    elif target < arr[mid]:
      end = mid - 1
    else:
      return mid
  
  return None

# 리스트에서 target의 원소 개수를 찾을 때 upper - lower
# target이 나타나는 첫 번재 인덱스
def lower(target, arr, start, end):
  while start <= end:
    mid = (start + end) // 2

    if target > arr[mid]:
      start = mid + 1
    else:
      end = mid - 1
  
  return start

# target이 나타나는 가장 마지막 인덱스 + 1
def upper(target, arr, start, end):
  while start <= end:
    mid = (start + end) // 2

    if target >= arr[mid]:
      start = mid + 1
    else:
      end = mid - 1

  return start
