def insert(n: int, m: int, j: int, i: int) -> int:
  ones = ~0                # 11111111
  left = ones << (j+1)     # 11100000
  right = (1 << i) - 1     # 00000100 => 00000011
  mask = left | right      # 11100011
  mask &= n                # nnn000nn
  m <<= i
  return mask | m          # nnnmmmnn
