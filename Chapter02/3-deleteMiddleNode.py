from Node import Node
"""
Time Complexity O(1)
Space Complexity O(1)
"""
def deleteMiddleNode(node: 'Node') -> bool:
  if not node or not node.next:
    return False
  node.val = node.next.val
  node.next = node.next.next
  return True
