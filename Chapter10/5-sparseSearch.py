from typing import List

def search(arr: List[int], word: str) -> int:
  l, r = 0, len(arr) - 1

  while l <= r:
    m = l + (r-l)//2

    if arr[m] == '':
      ml = m - 1
      mr = m + 1
      while True:
        if ml < l and mr > r:
          return -1
        if ml >= l and arr[ml] != '':
          m = ml
          break
        elif mr <= r and arr[mr] != '':
          m = mr
          break
        ml -= 1
        mr += 1

    if arr[m] == word:
      return m
    elif word < arr[m]:
      r = m - 1
    else:
      l = m + 1
  return -1



print(search(['at','','','','ball','','','car','','','dad','',''], 'ball'))
print(search(['at','','','','ball','','','car','','','dad','',''], ''))
