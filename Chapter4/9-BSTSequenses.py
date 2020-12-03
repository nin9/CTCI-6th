from typing import List

class Node:
  def __init__(self, val:int=0, right:'Node'=None, left:'Node'=None) -> None:
    self.val = val
    self.right = right
    self.left = left


def weaveLists(left, right, weaved, prefix):
  if not left or not right:
    weaved.append(prefix + left + right)
    return
  weaveLists(left[1:], right, weaved, prefix + [left[0]])
  weaveLists(left, right[1:], weaved, prefix + [right[0]])


def BSTSequenses(root: 'Node') -> List[List[int]]:
  result = []
  if not root:
    result.append([])
    return result

  prefix = [root.val]

  left = BSTSequenses(root.left)
  right = BSTSequenses(root.right)

  for l in left:
    for r in right:
      weaved = []
      weaveLists(l, r, weaved, prefix)
      result.extend(weaved)

  return result



root = Node(6)
root.left = Node(3)
root.right = Node(9)
root.left.left = Node(1)
root.left.right = Node(4)

print(BSTSequenses(root))