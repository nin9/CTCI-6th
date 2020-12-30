def countWays(exp: str, result: bool, memo) -> int:
  if len(exp) == 0: return 0
  if len(exp) == 1: return 1 if bool(exp) == result else 0

  if exp + str(result) in memo: return memo[exp + str(result)]

  ways = 0
  for i in range(1, len(exp), 2):
    left = exp[:i]
    right = exp[i+1:]

    leftTrue = countWays(left, True, memo)
    leftFalse = countWays(left, False, memo)
    rightTrue = countWays(right, True, memo)
    rightFalse = countWays(right, False, memo)

    total = (leftTrue + leftFalse) * (rightTrue + rightFalse)

    totalTrue = 0
    if exp[i] == '|':
      totalTrue = leftTrue * rightTrue + leftFalse * rightTrue + leftTrue * rightFalse
    elif exp[i] == '&':
      totalTrue =  leftTrue * rightTrue
    elif exp == '^':
      totalTrue = leftTrue * rightFalse + leftFalse * rightTrue

    subways = totalTrue if result else (total - totalTrue)
    ways += subways

  memo[exp + str(result)] = ways
  return ways


def evaluate(exp: str, result: bool) -> int:
  memo = {}
  return countWays(exp, result, memo)


print(evaluate('1^0|0|1', False))
