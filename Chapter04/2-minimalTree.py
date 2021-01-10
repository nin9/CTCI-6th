from typing import List

class Node:
  def __init__(self, val: int = 0, left: 'Node' = None , right: 'Node' = None) -> None:
    self.val = val
    self.left = left
    self.right = right


def minimalTree(arr: List[int]) -> 'Node':
  if not arr: return None

  def minimalTreeRec(l: int, h: int) -> 'Node':
    if l > h:
      return None
    m = l + (h - l)//2

    root = Node(arr[m])
    root.right = minimalTreeRec(m+1, h)
    root.left = minimalTreeRec(l, m-1)

    return root

  return minimalTreeRec(0, len(arr)-1)
