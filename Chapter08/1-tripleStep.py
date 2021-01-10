def tripleStep(n: int) -> int:
  if n <= 0:
    return 0

  first, second, third = 1, 2, 4

  for _ in range(4, n):
    temp = first + second + third
    first = second
    second = third
    third = temp

  return first + second + third
