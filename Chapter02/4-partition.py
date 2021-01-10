from Node import Node
"""
Time Complexity O(n)
Space Complexity O(1)
for both solutions
"""
def partition1(head: 'Node', x: int) -> 'Node':
  if not head: return

  leftStart = leftEnd = rightStart = rightEnd = None
  curr = head

  while curr:
    nxt = curr.next
    curr.next = None
    if curr.val < x:
      if not leftStart:
        leftStart = curr
        leftEnd = leftStart
      else:
        leftEnd.next = curr
        leftEnd = leftEnd.next
    else:
      if not rightStart:
        rightStart = curr
        rightEnd = rightStart
      else:
        rightEnd.next = curr
        rightEnd = rightEnd.next
    curr = nxt

  if not leftStart:
    return rightStart

  leftEnd.next = rightStart
  return leftStart


def partition2(head: 'Node', x: int) -> 'Node':
  curr = tail = head

  while curr:
    nxt = curr.next
    if curr.val < x:
      curr.next = head
      head = curr
    else:
      tail.next = curr
      tail = curr
    curr = nxt

  tail.next = None

  return head
