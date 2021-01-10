class Node:
  def __init__(self, val:int=0, right:'Node'=None, left:'Node'=None, parent:'Node'=None) -> None:
    self.val = val
    self.right = right
    self.left = left
    self.parent = parent

def leftMostChild(node: 'Node') -> 'Node':
  if not node: return None
  while node.left:
    node = node.left
  return node

"""
Time Complexity O(h), where h is the height of the tree
Space Complexity O(h)
"""
def successor(node: 'Node') -> 'Node':
  if not node: return None

  if node.right:
    return leftMostChild(node.right)
  child = node
  parent = node.parent
  while parent and parent.left != child:
    child = parent
    parent = parent.parent
  return parent
