class MultiStack:
  def __init__(self, stackSize: int) -> None:
    self.numsStacks = 3
    self.stackSize = stackSize
    self.arr = [None] * (stackSize * self.numsStacks)
    self.sizes = [0] * self.numsStacks

  def push(self, item: int, stackNum: int) -> None:
    if self.isFull(stackNum):
      raise Exception('Stack is full')
    self.sizes[stackNum] += 1
    self.arr[self.indexOfTop(stackNum)] = item

  def pop(self, stackNum: int) -> int:
    if self.isEmpty(stackNum):
      raise Exception('Stack is empty')
    index = self.indexOfTop(stackNum)
    item = self.arr[index]
    self.arr[index] = None
    self.sizes[stackNum] -= 1
    return item

  def peek(self, stackNum: int) -> int:
    if self.isEmpty(stackNum):
      raise Exception('Stack is empty')
    return self.arr[self.indexOfTop(stackNum)]

  def indexOfTop(self, stacNum: int) -> int:
    offset = stacNum * self.stackSize
    size = self.stackSize[stacNum]
    return offset + size - 1

  def isEmpty(self, stackNum: int) -> bool:
    return self.sizes[stackNum] == 0

  def isFull(self, stackNum: int) -> bool:
    return self.sizes[stackNum] == self.stackSize
