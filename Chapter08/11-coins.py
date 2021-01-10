from typing import List
"""
for both approaches
Time Complexity O(number of coins * n)
Space Complexity(number of coins * n), although recursion requires more memory for the call stack.
"""

# Top Down Memoization

def nWays(rem: int, coins: List[int], idx: int, cache: List[List[int]]) -> int:
  if rem == 0:
    return 1
  if idx == len(coins) or rem < coins[idx]:
    return 0
  if cache[idx][rem] != -1:
    return cache[idx][rem]

  ways = nWays(rem, coins, idx+1, cache) + nWays(rem - coins[idx], coins, idx, cache)

  cache[idx][rem] = ways
  return ways


def coinWays(n: int) -> int:
  coins = [1, 5, 10, 25]
  cache = [[-1 for i in range(n+1)] for _ in coins]
  return nWays(n, coins, 0, cache)


##############################################################################################################
# Bottom Up DP

def coinWays2(n: int) -> int:
  coins = [1, 5, 10, 25]
  dp = [[0 for i in range(n+1)] for _ in coins]

  for i in range(len(coins)):
    dp[i][0] = 1

  for rem in range(coins[0], n+1):
    for i in range(len(coins)):
      if i > 0:
        dp[i][rem] += dp[i-1][rem]
      if rem - coins[i] >= 0:
        dp[i][rem] += dp[i][rem - coins[i]]

  return dp[-1][-1]



print(coinWays(5))
print(coinWays2(5))
