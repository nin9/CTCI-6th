from typing import List

def floodFill(screen: List[List[int]], i: int, j: int, color: int, newColor: int):
  if i < 0 or i >= len(screen) or j < 0 or j >= len(screen[0]) or screen[i][j] != color:
    return
  screen[i][j] = newColor
  floodFill(screen, i+1, j, color, newColor)
  floodFill(screen, i-1, j, color, newColor)
  floodFill(screen, i, j+1, color, newColor)
  floodFill(screen, i, j-1, color, newColor)


def paintFill(screen: List[List[int]], r: int, c: int, newColor: int) -> List[List[int]]:
  if not screen: return None

  color = screen[r][c]
  floodFill(screen, r, c, color, newColor)
  return screen



screen = [
  [1, 2, 5],
  [2, 2, 4],
  [2, 8, 6]
]

print(paintFill(screen, 1, 1, 3))