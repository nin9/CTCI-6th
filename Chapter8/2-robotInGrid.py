from typing import List, Tuple, Set

def findPathRec(maze: List[List[bool]], i: int, j: int, path: List[Tuple[int]], visisted: Set[Tuple[int]]) -> bool:
  if i < 0 or i >= len(maze) or j < 0 or j >= len(maze[0]) or not maze[i][j]:
    return False

  if ((i,j)) in visisted:
    return False

  path.append((i,j))
  visisted.add((i,j))
  if i == len(maze) - 1 and j == len(maze[0]) - 1:
    return True
  return findPathRec(maze, i+1, j, path, visisted) or findPathRec(maze, i, j+1, path, visisted)


def findPath(maze: List[List[bool]]) -> List[Tuple[int]]:
  if not maze or not maze[0]:
    return None

  path = []
  visisted = set()
  isValid = findPathRec(maze, 0, 0, path, visisted)
  return path if isValid else []

maze = [
  [True, True, True],
  [True, False, True],
  [True, False, True]
]

print(findPath(maze))
