from typing import List
from collections import defaultdict


"""
Time Complexity O(nk), where n is the length of the array and k is the max length of a string in the array.
Space Complexity O(nk)
"""
def anagrams(arr: List[str]) -> List[str]:
  res = defaultdict(list)

  for s in arr:
    count = [0] * 26
    for c in s:
      count[ord(c) - ord('a')] += 1
    res[tuple(count)].append(s)
  return res.values()




print(anagrams(["eat","tea","tan","ate","nat","bat"]))
