from collections import defaultdict
from typing import Dict

class Node:
  def __init__(self, val:int=0, right:'Node'=None, left:'Node'=None) -> None:
    self.val = val
    self.right = right
    self.left = left


def countPathsWithSum(root: 'Node', sum: int, currSum: int, m: Dict[int, int]) -> int:
  if not root: return 0

  currSum += root.val
  numPaths = m[currSum - sum]
  if currSum == sum:
    numPaths += 1

  m[currSum] += 1
  numPaths += countPathsWithSum(root.left, sum, currSum, m)
  numPaths += countPathsWithSum(root.right, sum, currSum, m)
  m[currSum] -= 1
  return numPaths

"""
Time Complexity O(n)
Space Complexity O(h), where h is the height of the tree
"""
def pathsWihtSum(root: 'Node', sum: int) -> int:
  m = defaultdict(int)
  return countPathsWithSum(root, sum, 0 , m)


root = Node(1)
root.left = Node(3)
root.right = Node(9)
root.left.left = Node(1)
root.left.right = Node(4)

print(pathsWihtSum(root, 4))

# [3,1,2,4,-3,5,7,9]

# 3 => 1
# 1 => 2
# 4 => 2
# 2 => 1
# 6 => 5 #2
# 10 => 5
# 7 => 6
# 12 => 7