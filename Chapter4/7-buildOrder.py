from typing import List, Set
from enum import Enum

class State(Enum):
  NOT_VISITED = 0
  PARTIAL = 1
  VISITED = 2

class Node:
  def __init__(self, name: str, adjacent: List['Node'] = []) -> None:
    self.name = name
    self.state = State.NOT_VISITED
    self.adjacent = []

class Graph:
  def __init__(self, nodes: List['Node'] = []) -> None:
    self.nodes = nodes

"""
Time Complexity O(e+n), where e is the number of edges and n is the number of nodes
Space Complexity O(n)
"""
def topologicalSort(node: 'Node', order: List['Node']) -> bool:
  if node.state == State.PARTIAL:
    return False

  if node.state == State.NOT_VISITED:
    node.state = State.PARTIAL
    for n in node.adjacent:
      if not topologicalSort(n, order):
        return False
    node.state = State.VISITED
    order.append(node.name)
  return True

def buildOrder(g: 'Graph') -> List['Node']:
  order = []
  for node in g.nodes:
    if node.state == State.NOT_VISITED:
      if not topologicalSort(node, order):
        return []
  order.reverse()
  return order



a = Node('a', [])
b = Node('b', [])
c = Node('c', [])
d = Node('d', [])
e = Node('e', [])
f = Node('f', [])

a.adjacent.append(d)
b.adjacent.append(d)
d.adjacent.append(c)
# c.adjacent.append(d) # cycle
f.adjacent.extend([a, b])
graph = Graph()
graph.nodes.extend([a, b, c, d, e, f])
print(buildOrder(graph))