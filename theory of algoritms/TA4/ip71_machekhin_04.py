print('Введите название файла:')
fd = open(input(), 'r')
data = list(map(lambda x: int(x), fd.read().split('\n')))
fd.close()

def N_digit(number, n):
  return int(number % pow(10, n) // pow(10, n - 1))

countOfDigits = 0
maxN = max(data)
countOfDigits = 0
while (maxN // 10 != 0):
  countOfDigits += 1
  maxN = maxN // 10

def Radix_Sort(A, d):
  A = Counting_Sort(A, d)
  print(A)
  if d == countOfDigits:
    return A
  if d <= countOfDigits:
    return Radix_Sort(A, d + 1)

def Counting_Sort(A, d):
  B = []
  C = []
  for i in range(0, 10):
    C.append([0, []])
  for i in range(0, len(A)):
    B.append(0)
    digit = N_digit(A[i], d)
    C[digit][0] += 1
    C[digit][1].append(A[i])
  for i in range(1, 10):
    C[i][0] += C[i - 1][0]
  for i in range(len(A) - 1, -1, -1):
    B[C[N_digit(A[i], d)][0] - 1] = C[N_digit(A[i], d)][1].pop(len(C[N_digit(A[i], d)][1]) - 1)
    C[N_digit(A[i], d)][0] -= 1
  return B

B = Radix_Sort(data, 1)
fd = open('ip71_machekhin_04_output.txt', 'w')
for i in range(0, len(B)):
  fd.write(str(B[i]) + '\n')
fd.close()