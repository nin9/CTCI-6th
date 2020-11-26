from collections import Counter
"""
Time Complexity O(n)
Space Complexity O(n)
"""
def checkPermutaion(s1: str, s2: str)-> bool:
  if len(s1) != len(s2):
    return False
  c1 = Counter(s1)

  for c in s2:
    if c not in c1 or c1[c]-1 < 0:
      return False
    c1[c]-=1

  return True
