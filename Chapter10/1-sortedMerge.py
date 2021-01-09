from typing import List

def merge(A: List[int], B: List[int]) -> List[int]:
  n, m = len(A), len(B)
  ptrB = m-1
  ptrA = n - m - 1
  i = n - 1

  while ptrB >= 0:
    if ptrA >= 0 and A[ptrA] > B[ptrB]:
      A[i] = A[ptrA]
      ptrA -= 1
    else:
      A[i] = B[ptrB]
      ptrB -= 1
    i -= 1

  return A


print(merge([11,15,18,0,0,0,0], [3,9,10,12]))
