"""
Time Complexity O(n)
Space Compexity O(1), because max length of set is the length of the alphabet
we could argue that using an array of length(vocabulary) is better because the set will likely need to expand its capacity at some point.
"""
# Approach 1
def isUnique1(s: str) -> bool:
  seen = set()
  for c in s:
    if c in seen:
      return False
    seen.add(c)

  return True

####################################################

"""
Time Complexity O(n)
Space Compexity O(1)
"""
# Approach 2
def isUnique2(s: str) -> bool:
  bitVector = 0
  for c in s:
    bitIndex = ord(c) - ord('a')
  
    if bitVector & (1 << bitIndex) > 0:
      return False
    bitVector = bitVector | (1 << bitIndex)
  
  return True
