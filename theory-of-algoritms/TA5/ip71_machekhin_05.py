from minHeap import minHeap
from maxHeap import maxHeap

HEAPS_ARITY = 2

print('Введите имя файла:')
fileName = 'input.txt'
fd = open(fileName, 'r')
countElements = int(fd.readline())
arr = list(map(lambda x: int(x), fd.readlines()))
fd.close()
print(arr)

fd = open('ip71_machkhin_05output.txt', 'w')

maxHeap = maxHeap(arr[0])
minHeap = minHeap()

fd.write(str(arr[0]) + '\n')

for number in arr[1:]:
  if maxHeap.storage[0] > number:
    maxHeap.insert(number)
  else:
    minHeap.insert(number)
  if maxHeap.countNodes - 1 > minHeap.countNodes:
    minHeap.insert(maxHeap.extractMax())
  elif minHeap.countNodes - 1 > maxHeap.countNodes:
    maxHeap.insert(minHeap.extractMin())
  if maxHeap.countNodes == minHeap.countNodes:
    fd.write(str(maxHeap.storage[0]) + ' ' + str(minHeap.storage[0]) + '\n')
  elif maxHeap.countNodes > minHeap.countNodes:
    fd.write(str(maxHeap.storage[0]) + '\n')
  else:
    fd.write(str(minHeap.storage[0]) + '\n')