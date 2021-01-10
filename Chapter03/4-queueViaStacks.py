class Queue:
  def __init__(self):
    self.pushStack = []
    self.popStack = []
    self.top = None

  def enqueue(self, item: int) -> None:
    self.pushStack.append(item)
    if len(self.pushStack) == 1:
      self.top = item

  def dequeue(self) -> int:
    self.shiftStacks()
    return self.popStack.pop()

  def shiftStacks(self) -> None:
    while self.pushStack:
      self.popStack.append(self.pushStack.pop())

  def peek(self) -> int:
    self.shiftStacks()
    return self.popStack[-1]

  def isEmpty(self) -> bool:
    return self.size() == 0

  def size(self) -> int:
    return len(self.popStack) + len(self.pushStack)
