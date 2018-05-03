data = []
print("Введите имя файла:")
fd = open(input())
line = fd.readline().replace('\n', '').split(' ')
countOfPeople = int(line[0])
countOfFilms = int(line[1])
line = fd.readline()
while line:
  data.append(list(map(lambda x: int(x), line.replace('\n', '').split(' '))))
  line = fd.readline()
fd.close()

print('Введите номер пользователя сайтом:')
number = int(input())
specialUser = data.pop(number - 1)

def sortAndCountInv(A, p, r):
  if p == r :
    return 0
  else:
    leftInv = sortAndCountInv(A, p, (p + r) // 2)
    rightInv = sortAndCountInv(A, (p + r) // 2 + 1, r)
    splitInv = mergeAndCountSplitInv(A, p, (p + r) // 2, r)
    return leftInv + rightInv + splitInv

def mergeAndCountSplitInv(A, p, q, r):
  n1 = q - p + 1
  n2 = r - q
  L = []
  R = []
  i = 0
  j = 1
  while i < n1:
    L.append(A[p + i])
    i += 1
  while j <= n2:
    R.append(A[q + j])
    j += 1
  L.append(float('Inf'))
  R.append(float('Inf'))
  i = 0
  j = 0
  c = 0
  k = p
  while k <= r:
    if L[i] <= R[j]:
      A[k] = L[i]
      i += 1
    else:
      A[k] = R[j]
      j += 1
      c += n1 - i
    k += 1
  return c

for n in range(countOfPeople - 1):
  data[n] = [
    n + 1 if n + 1 < number else n + 2,
    sortAndCountInv(
      list(map(
      lambda x: data[n][1:][specialUser[1:].index(specialUser[1:].index(x) + 1)], 
      specialUser[1:]
    )), 0, countOfFilms - 1)
  ]

def mergeSort(A, p, r):
  if p < r:
    mergeSort(A, p, (p + r) // 2)
    mergeSort(A, (p + r) // 2 + 1, r)
    merge(A, p, (p + r) // 2, r)

def merge(A, p, q, r):
  n1 = q - p + 1
  n2 = r - q
  L = []
  R = []
  for i in range(p, q + 1):
    L.append(A[i])
  for i in range(q + 1, r + 1):
    R.append(A[i])
  L.append([1, float('Inf')])
  R.append([1, float('Inf')])
  i = 0
  j = 0
  for k in range(p, r + 1):
    if L[i][1] > R[j][1]:
      A[k] = R[j]
      j += 1
    else:
      A[k] = L[i]
      i += 1

fd = open('ip71_machechin_02.txt', 'w')
fd.write(str(number) + '\n')
for i in data:
  fd.write(str(i[0]) + ' ' + str(i[1]) + '\n')
fd.write(str(number) + '\n')
fd.close()