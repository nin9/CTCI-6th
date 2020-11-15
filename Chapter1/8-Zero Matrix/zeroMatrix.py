from typing import List
"""
Time Complexity O(nm)
Space Complexity O(n+m)
"""
# Approach 1
def zeroMatix1(matrix: List[List[int]]) -> List[List[int]]:
  if not matrix: return
  r, c = len(matrix), len(matrix[0])

  rows, columns = set(), set()
  for i in range(r):
    for j in range(c):
        if matrix[i][j] == 0:
            rows.add(i)
            columns.add(j)

  for i in range(r):
    for j in range(c):
      if i in rows or j in columns:
          matrix[i][j] = 0

  return matrix

######################################################################################

"""
Time Complexity O(nm)
Space Complexity O(1)
"""
# Approach 2
def zeroMatix2(matrix: List[List[int]]) -> List[List[int]]:
  if not matrix: return
  r, c = len(matrix), len(matrix[0])

  rowHasZero, colHasZero = False, False

  for j in range(c):
    if matrix[0][j] == 0:
      rowHasZero = True
      break
  for i in range(r):
    if matrix[i][0] == 0:
      colHasZero = True
      break
    
  for i in range(1, r):
    for j in range(1, c):
      if matrix[i][j] == 0:
        matrix[0][j] = 0
        matrix[i][0] = 0

  for j in range(c):
    if matrix[0][j] == 0:
      nullifyCol(matrix, j)

  for i in range(r):
    if matrix[i][0] == 0:
      nullifyRow(matrix, i)

  if rowHasZero:
    nullifyRow(matrix, 0)

  if colHasZero:
    nullifyCol(matrix, 0)

    return matrix


def nullifyRow(matrix: List[List[int]], row: int) -> None:
  for j in range(len(matrix[0])):
    matrix[row][j] = 0

def nullifyCol(matrix: List[List[int]], col: int) -> None:
  for i in range(len(matrix)):
    matrix[i][col] = 0

