from Node import Node
"""
Time Complexity O(n)
Space Complexity O(1)
"""
def loopDetection(head: 'Node') -> 'Node':
  slow = fast = head

  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      slow = head
      while slow != fast:
        slow = slow.next
        fast = fast.next
      return slow
  return None
