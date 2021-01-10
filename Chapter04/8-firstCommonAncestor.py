class Node:
  def __init__(self, val:int=0, right:'Node'=None, left:'Node'=None) -> None:
    self.val = val
    self.right = right
    self.left = left


"""
Time Complexity O(n)
Space Complexity O(n)
"""
def helper(root: 'Node', p: 'Node', q: 'Node') -> ('Node', bool):
  if not root: return (None, False)

  checkLeft = helper(root.left, p, q)
  checkRight = helper(root.right, p, q)

  if root in [p, q]:
    isAncestor = checkLeft[0] or checkRight[0]
    return (root, isAncestor)
  if (checkLeft[0] and checkRight[0]):
    return (root, True)
  if checkLeft[0]:
    return checkLeft
  return checkRight

def firstCommonAncestor(root: 'Node', p: 'Node', q: 'Node') -> bool:
  isAncestor = helper(root, p, q)
  if isAncestor[1]:
    return isAncestor[0]
  return None



root = Node(6)
root.left = Node(3)
root.right = Node(9)
root.left.left = Node(1)
root.left.right = Node(4)

print(firstCommonAncestor(root, root.left.left, root.left.right).val)
print(firstCommonAncestor(root, root.left.left, Node(7)))