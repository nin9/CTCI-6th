def rlshift(val: int, n: int) -> int:
  return val>>n if val >= 0 else (val+0x100000000)>>n