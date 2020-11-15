"""
Time Complexity O(n)
Space Complexity O(1)
"""
# Approach 1
def stringRotation1(s1: str, s2: str) -> bool:
  if len(s1) != len(s2): return False

  i = 0
  while i < len(s2) and s2[i] != s1[0]:
    i+=1

  j = i
  k = 0
  while j < len(s2):
    if s2[j] != s1[k]:
      return False
    j+=1
    k+=1
  return s2 in s1
  # return isSubstring(s2[:i], s1)

#########################################################

"""
Time Complexity O(n)
Space Complexity O(1)
"""
# Approach 2: more elegant
def stringRotation2(s1: str, s2: str) -> bool:
  if len(s1) != len(s2): return False

  s1s1 = s1+s1

  return s2 in s1s1
  # return isSubstring(s2, s1s1)
