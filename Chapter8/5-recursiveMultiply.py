"""
Time Complexity O(logs), where s is the smaller number
Space Complexity O(1)
"""
def minProduct(smaller: int, bigger: int) -> int:
  if smaller == 0:
    return 0

  if smaller == 1:
    return bigger

  ans = 0
  if smaller % 2 == 1:
    ans += bigger

  halfPord = minProduct(smaller>>1, bigger)

  return ans + halfPord + halfPord


def multiply(n: int, m: int) -> int:
  smaller = n if n < m else m
  bigger = n if n > m else m
  return minProduct(smaller, bigger)


print(multiply(0, 4))
