from util import rlshift

def flipBit(n: int) -> int:
  if ~n == 0:
    return 32
  currLength = prevLength = 0
  maxLength = 1

  while n != 0:
    if n & 1 == 1:
      currLength += 1
    elif n & 1 == 0:
      prevLength = 0 if n & 2 == 0 else currLength
      currLength = 0

    maxLength = max(currLength + prevLength + 1, maxLength)
    n = rlshift(n, 1)
  return maxLength

print(flipBit(1775)) # 11011101111
