from typing import List

class Listy:
  def __init__(self, arr: List[int]):
    self.list = arr

  def elementAt(self, index):
    if index >= len(self.list):
      return -1
    return self.list[index]


def search(listy: Listy, x: int) -> int:
  idx = 1
  while listy.elementAt(idx) != -1 and listy.elementAt(idx) < x:
    idx *= 2

  l, r = idx//2, idx
  while l <= r:
    m = l + (r-l)//2
    if listy.elementAt(m) == -1 or x < listy.elementAt(m):
      r = m - 1
    elif x > listy.elementAt(m):
      l = m + 1
    else:
      return m
  return -1


listy = Listy([2,5,5,7,10,15,20,27,31])
print(search(listy, 5))