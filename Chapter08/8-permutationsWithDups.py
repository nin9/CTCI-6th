from typing import List, Set
from collections import Counter

def getPerms(m, prefix: str, length: str, ans: List[str]):
  if length == 0:
    ans.append(prefix)
    return

  for c in m:
    if m[c] > 0:
      m[c] -= 1
      getPerms(m, prefix+c, length-1, ans)
      m[c]+=1

def permutations(s: str)->List[str]:
  ans = []
  m = Counter(s)
  getPerms(m, '', len(s), ans)
  return ans

print(permutations('aabbbc'))
