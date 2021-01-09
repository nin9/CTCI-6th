from typing import List

class BitSet:
  def __init__(self, size: int):
    self.bitset = [0] * (size >> 5)

  def get(self, pos) -> int:
    wordNumber = pos >> 5
    bitNumber = pos & 0x1f
    return (self.bitset[wordNumber] & (1 << bitNumber)) != 0


  def set(self, pos):
    wordNumber = pos >> 5
    bitNumber = pos & 0x1f
    self.bitset[wordNumber] |= (1 << bitNumber)



def findDuplicates(arr: List[int]):
  bitVector = BitSet(32000)
  for num in arr:
    bitNum = num - 1
    if bitVector.get(bitNum):
      print(num)
    else:
      bitVector.set(bitNum)




arr = [0] * 32000
for i in range(len(arr)):
  arr[i] = i + 1

arr[-1] = 5

findDuplicates(arr)
