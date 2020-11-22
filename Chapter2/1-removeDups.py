from Node import Node
"""
Time Complexity O(n)
Space Complexity O(n)
"""
def removeDups(head: 'Node') -> 'Node':
  if not head: return head

  seen = set()
  seen.add(head.val)

  curr = head
  prev = None
  while curr:
    if curr.val in seen:
      prev.next = curr.next
    else:
      seen.add(curr.val)
      prev = curr
    curr = curr.next

  return head
