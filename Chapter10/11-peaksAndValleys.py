from typing import List

"""
Time Complexity O(nlogn)
Space Complexity O(1)
"""
# Approach 1
def sortPeakValley(arr: List[int]) -> List[int]:
  arr.sort()
  n = len(arr)

  for i in range(1,n,2):
    arr[i], arr[i-1] = arr[i-1], arr[i]
  return arr

####################################################
"""
Time Complexity O(n)
Space Complexity O(1)
"""
# Approach 2
def sortPeakValley2(arr: List[int]) -> List[int]:
  n = len(arr)

  for i in range(1,n-1,2):
    if arr[i] > arr[i+1] and arr[i] > arr[i-1]:
      continue # arr[i] is already a peak
    if arr[i+1] > arr[i-1]:
      arr[i], arr[i+1] = arr[i+1], arr[i]
    else:
      arr[i], arr[i-1] = arr[i-1], arr[i]
  return arr


arr = [5,3,1,2,3]
print(sortPeakValley(arr))
print(sortPeakValley2(arr))
