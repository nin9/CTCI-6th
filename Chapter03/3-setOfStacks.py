class Node:
  def __init__(self, val=0, above=None, below=None):
    self.val = val
    self.above = above
    self.below = below


class Stack:
  def __init__(self, capacity: int) -> None:
    self.capacity = capacity
    self.top = None
    self.bottom = None
    self.size = 0

  def join(self, above: 'Node', below: 'Node') -> None:
    if below: below.above = above
    if above: above.below = below

  def push(self, item: int) -> None:
    if self.isFull():
      raise Exception('Stack is full')
    node = Node(item)
    self.size += 1
    if self.size == 1:
      self.bottom = node
    self.join(node, self.top)
    self.top = node

  def pop(self) -> int:
    if self.isEmpty():
      raise Exception('Stack is empty')
    item = self.top.val
    self.top = self.top.below
    self.size -= 1
    return item

  def removeBottom(self) -> int:
    if self.isEmpty():
      raise Exception('Stack is empty')
    item = self.bottom.val
    self.bottom = self.bottom.above
    if self.bottom: self.bottom.below = None
    self.size -= 1
    return item

  def isEmpty(self) -> bool:
    return self.size == 0

  def isFull(self) -> bool:
    return self.size >= self.capacity


class SetOfStacks:
  def __init__(self, capacity: int) -> None:
    self.capacity = capacity
    self.stacks = []

  def push(self, item: int) -> None:
    last = self.getLastStack()
    if not last or last.isFull():
      stack = Stack(self.capacity)
      stack.push(item)
      self.stacks.append(stack)
    else:
      last.push(item)

  def pop(self) -> int:
    last = self.getLastStack()
    if not last:
      raise Exception('Stack is empty')
    item = last.pop()
    if last.isEmpty():
      self.stacks.pop()
    return item

  def getLastStack(self) -> 'Stack':
    if not self.stacks:
      return None
    return self.stacks[-1]

  def popAtIndex(self, index: int) -> int:
    return self.leftShift(index, True)

  def leftShift(self, index: int, removeTop: bool) -> int:
    stack = self.stacks[index]
    removedItem = stack.pop() if removeTop else stack.removeBottom()
    if stack.isEmpty():
      self.stacks.pop(index)
    elif len(self.stacks) > index + 1:
      val = self.leftShift(index + 1, False)
      stack.push(val)
    return removedItem
