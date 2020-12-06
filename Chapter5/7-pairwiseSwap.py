from util import rlshift

def swap(n: int) -> int:
  oddMask = 0xaaaaaaaa
  evenMask = 0x55555555

  even = n & evenMask
  even << 1

  odd = oddMask & n
  odd = rlshift(odd, 1)

  return even | odd