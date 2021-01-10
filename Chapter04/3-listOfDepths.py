from collections import deque
from typing import List

class Node:
  def __init__(self, val:int=0, right:'Node'=None, left:'Node'=None) -> None:
    self.val = val
    self.right = right
    self.left = left


def createLevelListDFS(root: 'Node', level: int, lists: List[List['Node']]) -> None:
  if not root: return

  if level == len(lists):
    l = []
    lists.append(l)
  else:
    l = lists[level]

  l.append(root)
  createLevelListDFS(root.left, level+1, lists)
  createLevelListDFS(root.right, level+1, lists)

def createLevelListBFS(root: 'Node', lists: List[List['Node']]) -> None:
  if not root: return

  queue = deque()
  queue.append(root)

  while queue:
    size = len(queue)
    l = []
    for _ in range(size):
      node = queue.popleft()
      l.append(node)
      if node.left: queue.append(node.left)
      if node.right: queue.append(node.right)
    lists.append(l)


def createLevelList(root: 'Node') -> List[List['Node']]:
  lists = []
  createLevelListDFS(root, 0, lists)
  # createLevelListBFS(root, lists)
  return lists




root = Node(6)
root.left = Node(3)
root.right = Node(9)
root.left.left = Node(1)
root.left.right = Node(4)

lists = createLevelList(root)

for l in lists:
  for t in l:
    print(t.val, end =" ")
  print()
