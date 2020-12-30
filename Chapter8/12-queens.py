from typing import List

def backtrack(row: int, columns: List[List[int]], diag_right: List[int], diag_left: List[int], visited: List[int]):
  n = len(columns)
  if row == n:
    print(columns)
    return

  for col in range(n):
    if not visited[col] and not diag_right[row+col] and not diag_left[n+col-row]:
      visited[col] = diag_right[row+col] = diag_left[n+col-row] = 1
      columns[row] = col
      backtrack(row+1, columns, diag_right, diag_left, visited)
      columns[row] = 0
      visited[col] = diag_right[row+col] = diag_left[n+col-row] = 0



def queens(n = 8):
  columns = [0]*n
  visited = [0]*n
  diag_right = [0]*(2*n+1)
  diag_left = [0]*(2*n+1)

  backtrack(0, columns, diag_right, diag_left, visited)


queens(4)
