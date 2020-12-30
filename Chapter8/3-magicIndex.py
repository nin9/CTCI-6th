from typing import List

def findMagicIndex(arr: List[int], l: int, r: int) -> int:
  if l > r:
    return -1

  m = l + (r-l)//2
  if m == arr[m]:
    return m
  if m < arr[m]:
    return findMagicIndex(arr, l, m-1)
  else:
    return findMagicIndex(arr, m+1, r)


def magicIndex(arr: List[int]) -> int:
  return findMagicIndex(arr, 0, len(arr)-1)


print(magicIndex([-1,0,1,3,6]))

####################################################################
# Follow up

def findMagicIndex2(arr: List[int], l: int, r: int) -> int:
  if l > r:
    return -1

  m = l + (r-l)//2
  if m == arr[m]:
    return m

  leftEnd = min(m-1, arr[m])
  left = findMagicIndex(arr, l, leftEnd)
  if left > -1:
    return left

  rightStart = max(m+1, arr[m])
  right = findMagicIndex(arr, rightStart, r)

  if right > -1:
    return right


def magicIndex2(arr: List[int]) -> int:
  return findMagicIndex2(arr, 0, len(arr)-1)