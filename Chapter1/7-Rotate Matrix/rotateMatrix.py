from typing import List
"""
for both approaches
Time Complexity O(n^2)
Space Complexity O(1)
"""

# Approach 1
def rotateMarix1(matrix: List[List[int]]) -> None:
  if not matrix: return
  n = len(matrix)
  
  # Step 1: transpose the matrix
  for i in range(n):
    for j in range(i, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
          
  # Step 2: reverse the rows:
  for row in matrix:
    row.reverse()

# Approach 2
def rotateMarix2(matrix: List[List[int]]) -> None:
  if not matrix: return
  n = len(matrix)

  for layer in range(n//2):
    first = layer
    last = n - 1 - layer
    for i in range(first, last):
      offset = i - first
      top = matrix[first][i]                                  # top
      matrix[first][i] = matrix[last-offset][first]           # left -> top
      matrix[last-offset][first] = matrix[last][last-offset]  # bottom -> left
      matrix[last][last-offset] = matrix[i][last]             # right -> bottom
      matrix[i][last] = top                                   # top -> right
