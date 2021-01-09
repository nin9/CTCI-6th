from typing import List

# Approach 1
def rotatedBinarySearch(arr: List[int], x: int, l: int, r: int) -> int:
  if l > r:
    return -1

  m = l + (r-l)//2

  if arr[m] == x:
    return m
  # arr[left to mid] is sorted
  if arr[l] < arr[m]:
    if x >= arr[l] and x < arr[m]:
      return rotatedBinarySearch(arr, x, l, m-1)
    else:
      return rotatedBinarySearch(arr, x, m+1, r)
  # arr[mide to right] is sorted
  elif arr[l] > arr[m]:
    if x > arr[m] and x <= arr[r]:
      return rotatedBinarySearch(arr, x, m+1, r)
    else:
      return rotatedBinarySearch(arr, x, l, m-1)
  elif arr[l] == arr[m]:
    if arr[r] != arr[m]:
      return rotatedBinarySearch(arr, x, m+1, r)
    else:
      res = rotatedBinarySearch(arr, x, l, m-1)
      if res == -1:
        return rotatedBinarySearch(arr, x, m+1, r)
      else:
        return res


def search(arr: List[int], x: int) -> int:
  return rotatedBinarySearch(arr, x, 0, len(arr)-1)

################################################################################
# Approach 2
def search2(arr: List[int], x: int) -> int:
  l, r = 0, len(arr) - 1

  while l <= r:
    # linear search
    while l < r and arr[l] == arr[l+1]: l+=1
    while l < r and arr[r] == arr[r-1]: r-=1

    m = l + (r-l)//2

    if arr[m] == x:
      return m
    # arr[left to mid] is sorted
    if arr[l] <= arr[m]:
      if x >= arr[l] and x < arr[m]:
        r = m - 1
      else:
        l = m + 1
    # arr[mid to right] is sorted
    else:
      if x > arr[m] and x <= arr[r]:
        l = m + 1
      else:
        r = m - 1
  return -1

################################################################################
# Approach 3
def search3(arr: List[int], x: int) -> int:
  l, r = 0, len(arr) - 1

  while l <= r:
    m = l + (r-l)//2

    if arr[m] == x:
      return m

    # linear search
    if arr[l] == arr[m]:
      l+=1
      continue

    # arr[left to mid] is sorted
    if arr[l] < arr[m]:
      if x >= arr[l] and x < arr[m]:
        r = m - 1
      else:
        l = m + 1
    # arr[mid to right] is sorted
    else:
      if x > arr[m] and x <= arr[r]:
        l = m + 1
      else:
        r = m - 1
  return -1

print(search([15,16,19,20,25,1,3,4,5,7,10,14], 5))
print(search2([15,16,19,20,25,1,3,4,5,7,10,14], 5))
print(search3([15,16,19,20,25,1,3,4,5,7,10,14], 5))