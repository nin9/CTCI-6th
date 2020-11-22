from Node import Node
"""
Time Complexity O(n)
Space Complexity O(1)
"""
def palindrom(head: 'Node') -> bool:
  slow = fast = head

  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next


  slow = reverse(slow)
  fast = head

  while slow:
    if slow.val != fast.val:
      return False
    slow = slow.next
    fast = fast.next

  return True


def reverse(head: 'Node') -> 'Node':
  curr = head
  prev = None

  while curr:
    nxt = curr.next
    curr.next = prev
    prev = curr
    curr = nxt
  return prev
