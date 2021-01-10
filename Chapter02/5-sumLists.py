from Node import Node
"""
for both solutions
Time Complexity O(n)
Space Complexity O(n)
"""
def sumLists(l1: 'Node', l2: 'Node') -> 'Node':
  carry = 0
  dummy = Node()
  l3 = dummy
  while l1 or l2:
    sum = carry
    if l1:
      sum += l1.val
      l1 = l1.next
    if l2:
      sum += l2.val
      l2 = l2.next

    l3.next = Node(sum%10)
    carry = sum//10

  if carry:
    l3.next = Node(carry)


  return dummy.next

###############################################################

def sumListsFollowUp(head1: 'Node', head2: 'Node')-> 'Node':
  l1 = reverse(head1)
  l2 = reverse(head2)

  return reverse(sumLists(l1, l2))

def reverse(head: 'Node') -> 'Node':
  curr = head
  prev = None

  while curr:
    nxt = curr.next
    curr.next = prev
    prev = curr
    curr = nxt
  return prev
