class Node:
  def __init__(self, val:int=0, right:'Node'=None, left:'Node'=None) -> None:
    self.val = val
    self.right = right
    self.left = left

# Approach 1
def checkBST(root: 'Node', minVal: int, maxVal: int) -> bool:
  if not root: return True

  if root.val <= minVal or root.val > maxVal:
    return False
  leftCheck = checkBST(root.left, minVal, root.val)
  rightCheck = checkBST(root.right, root.val, maxVal)

  return leftCheck and rightCheck

""""
Time Complexity O(n)
Space Complexity O(h), where h is the tree height
"""
def isBST(root: 'Node') -> bool:
  return checkBST(root, float('-inf'), float('inf'))

########################################################################
# Approach 2
"""
Time Complexity O(n)
Space Complexity O(h), where h is the tree height
"""

def isBST2(root: 'Node') -> bool:
  if not root: return True

  stack = []
  minVal = float('-inf')

  root
  while stack or root:
    while root:
      stack.append(root)
      root = root.left

    root = stack.pop()
    if root.val <= minVal: return False
    minVal = root.val
    root = root.right

  return True



root = Node(6)
root.left = Node(3)
root.right = Node(9)
root.left.left = Node(1)
root.left.right = Node(4)

print(isBST(root))