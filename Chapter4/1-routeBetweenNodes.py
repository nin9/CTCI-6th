from typing import List
from collections import deque

class Node:
  def __init__(self, name: str, adjacent: List['Node'] = []) -> None:
    self.name = name
    self.adjacent = []

class Graph:
  def __init__(self, nodes: List['Node'] = []) -> None:
    self.nodes = nodes


def routeBetweenNodes(start: 'Node', end: 'Node') -> bool:
  if start == end:
    return True
  queue = deque()
  visited = set()

  queue.append(start)
  visited.add(start)

  while queue:
    root = queue.popleft()
    for node in root.adjacent:
      if node not in visited:
        if node == end:
          return True
        visited.add(node)
        queue.append(node)
  return False
