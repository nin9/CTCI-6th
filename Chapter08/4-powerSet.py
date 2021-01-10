from typing import List

# Backtracing

def backtrack(arr: List[int], idx: int, subsets: List[List[int]], ans: List[List[int]]):
  ans.append(subsets[:])

  for i in range(idx, len(arr)):
    subsets.append(arr[i])
    backtrack(arr, i+1, subsets, ans)
    subsets.pop()


def powerSet(arr: List[int]) -> List[List[int]]:
  ans = []
  backtrack(arr, 0 ,[], ans)
  return ans

print(powerSet([1, 2, 3]))

###################################################################################

# Iterative

def powerSet2(arr: List[int]) -> List[List[int]]:
  ans = [[]]

  for n in arr:
    ans += [t + [n] for t in ans]
  return ans


print(powerSet2([1, 2, 3]))

###################################################################################

# Bitmask

def convertIntToSet(arr: List[int], num: int):
  subset = []
  index = 0
  k = num
  while k > 0:
    if (k & 1) == 1:
      subset.append(arr[index])
    index += 1
    k >>= 1
  return subset

def powerSet3(arr: List[int]) -> List[List[int]]:
  ans = []
  max = 1 << len(arr)

  for i in range(max):
    subset = convertIntToSet(arr, i)
    ans.append(subset)
  return ans


print(powerSet3([1, 2, 3]))
