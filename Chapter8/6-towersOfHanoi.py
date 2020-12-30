from typing import List

def move(t1: List[int], t2: List[int], t3: List[int], n: int):
  if n == 1:
    t3.append(t1.pop())
  else:
    move(t1, t3, t2, n-1)
    t3.append(t1.pop())
    move(t2, t1, t3, n-1)



def hanoi(n: int):
  t1 = [i+1 for i in range(n)]
  t3 = []
  move(t1, [], t3, n)
  return t3

print(hanoi(5))