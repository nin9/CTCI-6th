from typing import List, Tuple

def createStack(boxes: List[Tuple[int]], idx: int, cache: List[int]) -> int:
  if idx < len(boxes) and cache[idx] > 0:
    return cache[idx]

  bottomBox = boxes[idx]
  maxHeight = 0
  for i in range(idx+1, len(boxes)):
    if boxes[i][0] < bottomBox[0] and boxes[i][1] < bottomBox[1] and boxes[i][2] < bottomBox[2]:
      height = createStack(boxes, i, cache)
      maxHeight = max(height, maxHeight)
  cache[idx] = bottomBox[2] + maxHeight
  return cache[idx]


def stackOfBoxes(boxes: List[Tuple[int]]) -> int:
  boxes.sort(key=lambda x:x [0], reverse=True)
  maxHeight = 0
  cache = [0] * len(boxes)
  for i in range(len(boxes)):
    height = createStack(boxes, i, cache)
    maxHeight = max(height, maxHeight)
  return maxHeight


boxes = [(1,3,2), (2,4,5), (3,4,4), (4,5,6), (5,6,3)]
print(stackOfBoxes(boxes))
