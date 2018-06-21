def insert(this, *keys):
  for key in keys:
    this.storage.append(key)
    curIndex = this.countNodes
    curParentIndex = (curIndex - 1) // 2
    while this.storage[curParentIndex] < key and curParentIndex >= 0:
      this.storageSWAP(curIndex, (curIndex - 1) // 2)
      curIndex = (curIndex - 1) // 2
      curParentIndex = (curIndex - 1) // 2
    this.countNodes += 1

def storageSWAP(this, index1, index2):
  temp = this.storage[index1]
  this.storage[index1] = this.storage[index2]
  this.storage[index2] = temp

def extractMax(this):
  if this.countNodes == 0:
    return float('inf')
  max = this.storage[0]
  sievingElement = this.storage.pop()
  this.countNodes -= 1
  if this.countNodes == 0:
    return max
  this.storage[0] = sievingElement
  curIndex = 0
  maxChildIndex = 0
  if this.countNodes > 1:
    maxChildIndex = 1
  if this.countNodes > 2 and this.storage[2] > this.storage[1]:
    maxChildIndex = 2
  while this.storage[maxChildIndex] > sievingElement:
    this.storageSWAP(maxChildIndex, curIndex)
    curIndex = curIndex * 2 + (1 if maxChildIndex % 2 == 1 else 2)
    if this.countNodes > curIndex * 2 + 1:
      maxChildIndex = curIndex * 2 + 1
    if this.countNodes > curIndex * 2 + 2 and this.storage[curIndex * 2 + 2] > this.storage[curIndex * 2 + 1]:
      maxChildIndex = curIndex * 2 + 2
  return max
    
class maxHeap:
  storage = []
  countNodes = 0
  def __init__(this, *keys):
    if keys:
      for key in keys:
        this.insert(key)
  extractMax = extractMax
  insert = insert
  storageSWAP = storageSWAP
  