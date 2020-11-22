from Node import Node
"""
Time Complexity O(n)
Space Complexity O(1)
"""
def kthToLast(head: 'Node', k: int) -> 'Node':
  slow, fast = head, head

  for _ in range(k):
    if not fast:
      return None
    fast = fast.next

  while fast:
    fast = fast.next
    slow = slow.next

  return slow
