from typing import List

def generateParens(n: int) -> List[str]:
  res = []
  backtrack('', 0, 0, res, n)
  return res


def backtrack(s: str, left: int, right: int, res: List[str], n: int):
  if len(s) == 2 * n:
    res.append(s)

  if left < n:
    backtrack(s + '(', left + 1, right, res, n)
  if right < left:
    backtrack(s + ')', left, right + 1, res, n)


print(generateParens(3))
