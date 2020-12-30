from typing import List, Set

def getPerms(prefix: str, reminder: str, ans: List[str]):
  if len(reminder) == 0:
    ans.append(prefix)

  for i in range(len(reminder)):
    before = reminder[:i]
    after = reminder[i+1:]
    c = reminder[i]
    getPerms(prefix+c, before+after, ans)

def permutations(s: str)->List[str]:
  ans = []
  getPerms('', s, ans)
  return ans

print(permutations('abc'))
