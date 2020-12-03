class Node:
  def __init__(self, val:int=0, right:'Node'=None, left:'Node'=None) -> None:
    self.val = val
    self.right = right
    self.left = left

def preOrder(root: 'Node', l) -> None:
  if not root:
    l.append('#')
    return

  l.append(str(root.val))
  preOrder(root.left, l)
  preOrder(root.right, l)

"""
Time Complexity O(n+m)
Space Complexity O(n+m)
"""
def checkSubtree(t1: 'Node', t2: 'Node') -> bool:
  listT1, listT2 = [], []
  preOrder(t1, listT1)
  preOrder(t2, listT2)

  s1 = " ".join(listT1)
  s2 = " ".join(listT2)
  return s2 in s1

#####################################################################
# Approach 2

def sameTree(r1: 'Node', r2: 'Node') -> bool:
  if not r1 and not r2:
    return True
  if not r1 or not r2:
    return False
  if r1.val != r2.val:
    return False
  return sameTree(r1.left, r2.left) and sameTree(r1.right, r2.right)

def subTree(r1: 'Node', r2: 'Node') -> bool:
  if not r1:
    return False
  if r1.val == r2.val and sameTree(r1, r2):
    return True
  return subTree(r1.left, r2) or subTree(r1.right, r2)

"""
Time Complexity O(n+km)
Space Complexity O(logn+logm)
"""
def checkSubtree2(t1: 'Node', t2: 'Node') -> bool:
  if not t2:
    return True
  return subTree(t1, t2)

root = Node(6)
root.left = Node(3)
root.right = Node(9)
root.left.left = Node(1)
root.left.right = Node(4)

root2 = Node(3)
root2.left = Node(1)
root2.right = Node(4)

print(checkSubtree(root, root2))
print(checkSubtree2(root, root2))