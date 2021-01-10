# Approach 1
def conversion(n: int, m: int) -> int:
  if n == m:
    return 0

  r = n ^ m
  count = 0

  while r != 0:
    if (r & 1) == 1:
      count += 1
    r >>= 1
  return count


# Approach 2
def conversion2(n: int, m: int) -> int:
  if n == m:
    return 0

  r = n ^ m
  count = 0

  while r != 0:
    r &= (r-1)
    count += 1
  return count

print(conversion(29, 15))
