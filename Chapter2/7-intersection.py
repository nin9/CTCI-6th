from Node import Node
"""
Time Complexity O(n+m)
Space Complexity O(1)
"""
def intersection(head1: 'Node', head2: 'Node') -> 'Node':
  l1 = head1
  l2 = head2

  while l1 != l2:
    l1 = l1.next if l1 else head2
    l2 = l2.next if l2 else head1

  return l1