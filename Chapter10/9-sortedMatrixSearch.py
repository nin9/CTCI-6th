from typing import List, Tuple


"""
Time Complexity O(r+c), where r is the number of rows and c is the number of columns
Space Complexity O(1)
"""
# Approach 1
def search(matrix: List[List[int]], target: int) -> Tuple[int]:
  if not matrix or len(matrix) == 0:
    return False
  
  i, j = 0, len(matrix[0]) - 1

  while i < len(matrix) and j >= 0:
    if matrix[i][j] == target:
      return True
    elif matrix[i][j] > target:
      j -= 1 # move left
    else:
      i += 1 # move down
  return False

###############################################################################################
# Approach 2
def binarySearch2D(matrix: List[List[int]], target: int, startRow: int, endRow: int, startCol: int, endCol: int) -> bool:
  if startRow > endRow or startCol > endCol:
    return False

  midRow = (startRow + endRow)//2
  midCol = (startCol + endCol)//2
  mid = matrix[midRow][midCol]

  if target == mid:
    return True

  if target < mid:
    return binarySearch2D(matrix, target, startRow, endRow, startCol, midCol-1,) or binarySearch2D(matrix, target, startRow, midRow-1, startCol, endCol)
  else:
    return binarySearch2D(matrix, target, startRow, endRow, midCol+1, endCol) or binarySearch2D(matrix, target, midRow+1, endRow, startCol, endCol)


def search2(matrix: List[List[int]], target: int) -> bool:
  if not matrix or len(matrix) == 0:
    return False

  endRow, endCol = len(matrix)-1, len(matrix[0])-1
  return binarySearch2D(matrix, target, 0, endRow, 0, endCol)



matrix = [
          [1, 2, 3],
          [5, 6, 7],
          [8, 9, 10]
        ]

print(search(matrix, 9))
print(search2(matrix, 9))
