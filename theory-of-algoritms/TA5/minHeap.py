def insert(this, *keys):
  for key in keys:
    this.storage.append(key)
    curIndex = this.countNodes
    curParentIndex = (curIndex - 1) // 2
    while this.storage[curParentIndex] > key and curParentIndex >= 0:
      this.storageSWAP(curIndex, (curIndex - 1) // 2)
      curIndex = (curIndex - 1) // 2
      curParentIndex = (curIndex - 1) // 2
    this.countNodes += 1

def storageSWAP(this, index1, index2):
  temp = this.storage[index1]
  this.storage[index1] = this.storage[index2]
  this.storage[index2] = temp

def extractMin(this):
  if this.countNodes == 0:
    return float('-inf')
  min = this.storage[0]
  sievingElement = this.storage.pop()
  this.countNodes -= 1
  if this.countNodes == 0:
    return min
  this.storage[0] = sievingElement
  curIndex = 0
  minChildIndex = 0
  if this.countNodes > 1:
    minChildIndex = 1
  if this.countNodes > 2 and this.storage[2] < this.storage[1]:
    minChildIndex = 2
  while this.storage[minChildIndex] < sievingElement:
    this.storageSWAP(minChildIndex, curIndex)
    curIndex = curIndex * 2 + (1 if minChildIndex % 2 == 1 else 2)
    if this.countNodes > curIndex * 2 + 1:
      minChildIndex = curIndex * 2 + 1
    if this.countNodes > curIndex * 2 + 2 and this.storage[curIndex * 2 + 2] < this.storage[curIndex * 2 + 1]:
      minChildIndex = curIndex * 2 + 2
  return min
    
class minHeap:
  storage = []
  countNodes = 0
  def __init__(this, *keys):
    if keys:
      for key in keys:
        this.insert(key)
  extractMin = extractMin
  insert = insert
  storageSWAP = storageSWAP
