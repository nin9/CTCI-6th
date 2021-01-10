from typing import List

"""
Time Complexity O(n^2)
Space Complexity O(n)
"""
def sortStack(stack: List[int]) -> List[int]:
  temp_stack = []

  while stack:
    item = stack.pop()
    while temp_stack and item < temp_stack[-1]:
      stack.append(temp_stack.pop())
    temp_stack.append(item)

  while temp_stack:
    stack.append(temp_stack.pop())

  return stack
