class Node:
  def __init__(self, val: int = 0, left: 'Node' = None , right: 'Node' = None) -> None:
    self.val = val
    self.left = left
    self.right = right
    self.leftSize = 0

  def insert(self, x: int):
    if x <= self.val:
      if not self.left:
        self.left = Node(x)
      else:
        self.left.insert(x)
      self.leftSize += 1
    else:
      if not self.right:
        self.right = Node(x)
      else:
        self.right.insert(x)

  def getRank(self, x: int) -> int:
    if x == self.val:
      return self.leftSize
    if x < self.val:
      if not self.left:
        return -1
      return self.left.getRank(x)
    else:
      rightRank = -1 if not self.right else self.right.getRank(x)
      if rightRank == -1:
        return - 1
      return self.leftSize + 1 + rightRank



def track(x: int):
  global root
  if not root:
    root = Node(x)
  else:
    root.insert(x)

def getRankOfNumber(x: int) -> int:
  return root.getRank(x)



root = None
stream = [5, 1, 4, 4, 5, 9, 7, 13, 3]

for i in stream:
  track(i)

print(getRankOfNumber(1))
print(getRankOfNumber(3))
print(getRankOfNumber(4))
