# Input:

data = []
print("Введите имя файла:")
fd = open(input(), 'r')
lineCounts = int(fd.readline())
data = list(map(lambda x: int(x), fd.read().split('\n')))
fd.close()

# Accessory: SWAP for two elements in the array:

def ArraySWAP(A, firstIndex, secondIndex):
  temp = A[firstIndex]
  A[firstIndex] = A[secondIndex]
  A[secondIndex] = temp

# Initialization of counters:

firstCounter = 0
secondCounter = 0
thirdCounter = 0

# 1) Simlle algoritms:

def Partition(A, p, r):
  global firstCounter
  x = A[r]
  i = p - 1
  for j in range(p, r):
    firstCounter += 1
    if A[j] <= x:
      i += 1
      ArraySWAP(A, j, i)
  ArraySWAP(A, i + 1, r)
  return i + 1

def QuickSort(A, p, r):
  if p < r:
    q = Partition(A, p, r)
    QuickSort(A, p, q - 1)
    QuickSort(A, q + 1, r)

# 2) Median:

def PartitionMedian(A, p, r):
  global secondCounter
  keysArray = [A[p], A[(p + r) // 2], A[r]]
  indexMax = keysArray.index(max(keysArray))
  pivot = max([keysArray[(indexMax + 1) % 3], keysArray[(indexMax + 2) % 3]])
  indexPivot = p if keysArray.index(pivot) == 0 else (
    (p + r) // 2 if keysArray.index(pivot) == 1 else r
  )
  ArraySWAP(A, r, indexPivot)
  i = p - 1
  for j in range(p, r):
    secondCounter += 1
    if A[j] <= pivot:
      i += 1
      ArraySWAP(A, j, i)
  ArraySWAP(A, i + 1, r)
  return i + 1

def QuickSortMedian(A, p, r):
  global secondCounter
  if p + 2 < r:
      q = PartitionMedian(A, p, r)
      QuickSortMedian(A, p, q - 1)
      QuickSortMedian(A, q + 1, r)
  else:
    secondCounter += SortTwoThreeElements(A, p, r)

# 3) With three pivots:

def Partition3(A, leftIndex, rightIndex):  
  global thirdCounter
  a = leftIndex + 2
  b = leftIndex + 2
  c = rightIndex - 1
  d = rightIndex - 1
  p = A[leftIndex]
  q = A[leftIndex + 1]
  r = A[rightIndex]
  while b <= c:
    while A[b] < q and b <= c:
      thirdCounter += 1
      if A[b] < p:
        ArraySWAP(A, a, b)
        a += 1
      b += 1
    thirdCounter += 1
    while A[c] > q and b <= c:
      thirdCounter += 1
      if A[c] > r:
        ArraySWAP(A, c, d)
        d -= 1
      c -= 1
    thirdCounter += 1
    if b <= c:
      thirdCounter += 1
      if A[b] > r:
        thirdCounter += 1
        if A[c] < p:
          ArraySWAP(A, b, a)
          ArraySWAP(A, a, c)
          a += 1
        else:
          ArraySWAP(A, b, c)
        ArraySWAP(A, c, d)
        b += 1
        c -= 1
        d -= 1
      else:
        thirdCounter += 1
        if A[c] < p:
          ArraySWAP(A, a, c)
          a += 1
        else:
          ArraySWAP(A, b, c)
        b += 1
        c -= 1
  a -= 1
  b -= 1
  c += 1
  d += 1
  ArraySWAP(A, leftIndex + 1, a)
  ArraySWAP(A, a, b)
  a -= 1
  ArraySWAP(A, leftIndex, a)
  ArraySWAP(A, rightIndex, d)

  return [a, b, d]

def QuickSort3(A, p, r):
  global thirdCounter
  if p + 2 < r:
    pivots = [A[p], A[p + 1], A[r]]
    SortTwoThreeElements(pivots, 0, 2)
    A[p] = pivots[0]
    A[p + 1] = pivots[1]
    A[r] = pivots[2]
    arrIndex = Partition3(A, p, r)
    QuickSort3(A, p, arrIndex[0] - 1)
    QuickSort3(A, arrIndex[0] + 1, arrIndex[1] - 1)
    QuickSort3(A, arrIndex[1] + 1, arrIndex[2] - 1)
    QuickSort3(A, arrIndex[2] + 1, r)
  else:
    thirdCounter += SortTwoThreeElements(A, p, r)
  
# Accessory: Sort of two - three elements:

def SortTwoThreeElements(A, p, r):
  counter = 0
  if p + 1 == r:
    counter += 1
    if A[p] > A[r]:
      ArraySWAP(A, p, r)
  elif p + 2 == r:
    counter += 1
    if A[p] > A[p + 1]:  # 213, 231, 321
      counter += 1
      if A[p] > A[r]:  # 231, 321
        counter += 1
        if A[p + 1] > A[r]:  # 321
          ArraySWAP(A, p, r)
        else:  # 231
          ArraySWAP(A, p, p + 1)
          ArraySWAP(A, p + 1, r)
      else:  # 213
        ArraySWAP(A, p, p + 1)
    elif A[p] > A[r]:  # 312
      counter += 1
      ArraySWAP(A, p, p + 1)
      ArraySWAP(A, p, r)
    elif A[r] < A[p + 1]:  # 132
      counter += 2
      ArraySWAP(A, p + 1, r)
    else: 
      counter += 3 # 123 (No change)
  return counter

A = list(data)
B = list(data)
C = list(data)
# Excecute:

QuickSort(A, 0, lineCounts - 1)
QuickSortMedian(B, 0, lineCounts - 1) 
QuickSort3(C, 0, lineCounts - 1)

# Output:

fd = open('ip_machekhin_03_output.txt', 'w')
fd.write(str(firstCounter) + ' ')
fd.close()
fd = open('ip_machekhin_03_output.txt', 'a')
fd.write(str(secondCounter) + ' ' + str(thirdCounter))