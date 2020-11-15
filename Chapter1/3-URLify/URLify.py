"""
Time Complexity O(n)
Space Complexity O(n) due to converting s to list
"""
def URLify(s: str, trueLength: int)-> str:
  s = list(s)
  idx = len(s)

  for i in reversed(range(trueLength)):
    if s[i] == " ":
      s[idx-3:idx] = '%20'
      idx-=3
    else:
        s[idx-1] = s[i]
        idx-=1
  return ''.join(s)
