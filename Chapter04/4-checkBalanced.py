class Node:
  def __init__(self, val:int=0, right:'Node'=None, left:'Node'=None) -> None:
    self.val = val
    self.right = right
    self.left = left

# Approach 1
def checkHeight(root: 'Node') -> int:
  if not root: return -1
  
  leftHeight = checkHeight(root.left)
  if leftHeight == float('-inf'): return leftHeight

  rightHeight = checkHeight(root.right)
  if rightHeight == float('-inf'): return rightHeight

  if abs(leftHeight - rightHeight) > 1: return float('-inf')
  return max(leftHeight, rightHeight) + 1

""""
Time Complexity O(n), where h is the height of the tree
Space Complexity O(1)
"""
def isBalanced(root: 'Node') -> bool:
  return checkHeight(root) != float('-inf')

############################################################
# Approach 2
""""
Time Complexity O(n), where h is the height of the tree
Space Complexity O(1)
"""
class Solution:
  def isBalanced(self, root: 'Node') -> bool:
    self.is_balanced = True

    def dfs(node: 'Node') -> int:
      if not node: return -1

      lh = dfs(node.left)
      rh = dfs(node.right)
      if abs(lh - rh) > 1:
        self.is_balanced = False
      return max(lh, rh) + 1

    dfs(root)
    return self.is_balanced