def binaryString(num: float) -> str:
  if num <= 0 or num >= 1:
    return 'ERROR'

  binary = []
  binary.append('.')

  while num > 0:
    if len(binary) >= 32:
      return 'ERROR'

    r = num*2
    if r >= 1:
      num = r-1
      binary.append('1')
    else:
      binary.append('0')
      num = r

  return ''.join(binary)
