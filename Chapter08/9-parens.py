from typing import List

def generateParens(n: int) -> List[str]:
  if n == 1:
    return ['()']

  parens = generateParens(n-1)
  res = []
  for p in parens:
    res.append(p +'()')
    if p + '()' != '()' + p:
      res.append('()' + p)
    res.append('(' + p + ')')
  return res

print(generateParens(3))
