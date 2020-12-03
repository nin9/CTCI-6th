from random import randrange

class Node:
  def __init__(self, val:int=0, right:'Node'=None, left:'Node'=None) -> None:
    self.val = val
    self.right = right
    self.left = left
    self.size = 1

  """
  Time Complexity O(logn)
  Space Complexity O(logn)
  """
  def getRandomNode(self) -> 'Node':
    leftSize = self.left.size if self.left else 0
    index = randrange(self.size)

    if index < leftSize:
      return self.left.getRandomNode()
    elif index == leftSize:
      return self
    else:
      return self.right.getRandomNode()


# Approach 2
  def getIthNode(self, index: int) -> 'Node':
    leftSize = self.left.size if self.left else 0
    if index < leftSize:
      return self.left.getIthNode(index)
    elif index == leftSize:
      return self
    else:
      return self.right.getIthNode(index - leftSize + 1)

  """
  Time Complexity O(logn)
  Space Complexity O(logn)
  """
  def getRandomNode2(self) -> 'Node':
    index = randrange(self.size)
    return self.getIthNode(index)

