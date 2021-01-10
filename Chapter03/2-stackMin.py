# Approach 1
class StackMin1:
  def __init__(self):
    self.stack = []

  def push(self, item: int) -> None:
    if self.isEmpty() :
      self.stack.append((item, item))
    else:
      topItem = self.peek()
      minItem = min(item, topItem)
      self.stack.append((item, minItem))

  def pop(self) -> int:
    if self.isEmpty():
      raise Exception('Stack is empty')
    item, _ = self.stack.pop()
    return item

  def peek(self) -> int:
    if self.isEmpty():
      raise Exception('Stack is empty')
    item, _ = self.stack[-1]
    return item

  def min(self) -> int:
    if self.isEmpty():
      raise Exception('Stack is empty')
    _, minItem = self.stack[-1]
    return minItem

  def isEmpty(self):
    return len(self.stack) == 0

############################################################

# Approach 2
class StackMin2:
  def __init__(self):
    self.stack = []
    self.minValues = []

  def push(self, item: int) -> None:
    if self.isEmpty() or item <= self.minValues[-1]:
      self.minValues.append(item)
    self.stack.append(item)

  def pop(self) -> int:
    if self.isEmpty():
      raise Exception('Stack is empty')
    item = self.stack.pop()
    if item == self.minValues[-1]:
      self.minValues.pop()
    return item

  def peek(self) -> int:
    if self.isEmpty():
      raise Exception('Stack is empty')
    return self.stack[-1]

  def min(self) -> int:
    if self.isEmpty():
      raise Exception('Stack is empty')
    return self.minValues[-1]

  def isEmpty(self):
    return len(self.stack) == 0
