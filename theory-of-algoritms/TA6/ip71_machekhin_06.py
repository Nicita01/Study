import sys as sys

MULT_HASHING_CONSTANT = 0.6180339887

# Считываем аргумент командной строки, дефолтно 1:
if len(sys.argv) > 1:
  numberHash = int(sys.argv[1])
else:
  numberHash = 1

# Считывание данных из даного файла
# Представление в виде массива элементов и массива сумм
fdInput = open('input.txt', 'r')
countsArray = fdInput.readline().split(' ')
arraySize = int(countsArray[0])
summsCount = int(countsArray[1])
array = []
summs = []
for i in range(0, arraySize):
  array.append(int(fdInput.readline()))
for i in range(arraySize, summsCount + arraySize):
  summs.append(int(fdInput.readline()))

fdOutput = open('ip71_machekhin_07_output.txt', 'w')

# Хэш-функция по методу деления
def hashFunctionDiv(key, storageSize):
  hash = key % storageSize
  return hash

# Хэш-функция по методу умножения
def hashFunctionMult(key, storageSize):
  hash = int(storageSize * ((key * MULT_HASHING_CONSTANT) % 1))
  return hash

# Функция для создания и заполнения файла с исходящими данными
def output(array):
  for curElement in array:
    for curItem in curElement:
      fdOutput.write(str(curItem) + ' ')
    fdOutput.write('\n')
  fdOutput.close()

# Функция по созданию хэш-таблицы с разрешением коллизий по методу цепочек
# и хэш-функцией по методу деления. Подсчитывание коллизий и поиск пар для сумм
def chainDiv(array, summs, arraySize):
  colizionCount = 0
  storageSize = 3 * arraySize
  hashStorage = [[] for curIndex in range(0, storageSize)]
  for curItem in array:
    hash = hashFunctionDiv(curItem, storageSize)
    lenChain = len(hashStorage[hash])
    colizionCount = colizionCount if lenChain == 0 else colizionCount + 1
    hashStorage[hash].append(curItem)
  pairs = [[colizionCount]]
  for curSumm in summs:
    flag = False
    for curItem in array:
      necessaryItem = curSumm - curItem
      hash = hashFunctionDiv(necessaryItem, storageSize)
      necessaryChain = hashStorage[hash]
      for curChaineElement in necessaryChain:
        if curChaineElement == necessaryItem:
          pairs.append([curItem, necessaryItem])
          flag = True
          break
      if flag:
        break
    if not flag:
      pairs.append([0, 0])
  return pairs

# Функция по созданию хэш-таблицы с разрешением коллизий по методу цепочек
# и хэш-функцией по методу умножения. Подсчитывание коллизий и поиск пар для сумм
def chainMult(array, summs, arraySize):
  colizionCount = 0
  storageSize = 3 * arraySize
  hashStorage = [[] for curIndex in range(0, storageSize)]
  for curItem in array:
    hash = hashFunctionMult(curItem, storageSize)
    lenChain = len(hashStorage[hash])
    colizionCount = colizionCount if lenChain == 0 else colizionCount + 1
    hashStorage[hash].append(curItem)
  pairs = [[colizionCount]]
  for curSumm in summs:
    flag = False
    for curItem in array:
      necessaryItem = curSumm - curItem
      hash = hashFunctionMult(necessaryItem, storageSize)
      necessaryChain = hashStorage[hash]
      for curChaineElement in necessaryChain:
        if curChaineElement == necessaryItem:
          pairs.append([curItem, necessaryItem])
          flag = True
          break
      if flag:
        break
    if not flag:
      pairs.append([0, 0])
  return pairs

# Функция по созданию хэш-таблицы с разрешением коллизий
# по методу открытой адресации и хэш-функцией по методу деления.
# Таблица использует линейное пробирование
# Подсчитывание коллизий и поиск пар для сумм
def openAdressingLinear(array, summs, arraySize):
  colizionCount = 0
  storageSize = arraySize * 3
  hashStorage = [0] * storageSize
  for curItem in array:
    supportHash = hashFunctionDiv(curItem, storageSize)
    i = 0
    while True:
      hash = hashFunctionDiv(supportHash + i, storageSize)
      if hashStorage[hash]:
        colizionCount += 1
        i += 1
      else:
        hashStorage[hash] = curItem
        break
  pairs = [[colizionCount]]
  for curSumm in summs:
    flag = False
    for curItem in array:
      necessaryItem = curSumm - curItem
      supportHash = hashFunctionDiv(necessaryItem, storageSize)
      i = 0
      currentTest = hashStorage[supportHash]
      while currentTest:
        hash = hashFunctionDiv(supportHash + i, storageSize)
        if currentTest == necessaryItem:
          pairs.append([curItem, necessaryItem])
          flag = True
          break
        else:
          i += 1
          currentTest = hashStorage[0 if hash + 1 == storageSize else hash + 1]
      if flag:
        break
    if not flag:
      pairs.append([0, 0])
  return pairs

# Функция по созданию хэш-таблицы с разрешением коллизий
# по методу открытой адресации и хэш-функцией по методу деления.
# Таблица использует квадратическое пробирование
# Подсчитывание коллизий и поиск пар для сумм
def openAdressingQuadratic(array, summs, arraySize):
  colizionCount = 0
  storageSize = arraySize * 3
  hashStorage = [0] * storageSize
  for curItem in array:
    supportHash = hashFunctionDiv(curItem, storageSize)
    i = 0
    while True:
      hash = hashFunctionDiv(supportHash + i, storageSize)
      if hashStorage[hash]:
        colizionCount += 1
        i += 1
      else:
        hashStorage[hash] = curItem
        break
  pairs = [[colizionCount]]
  for curSumm in summs:
    flag = False
    for curItem in array:
      necessaryItem = curSumm - curItem
      supportHash = hashFunctionDiv(necessaryItem, storageSize)
      i = 0
      currentTest = hashStorage[supportHash]
      while currentTest:
        hash = hashFunctionDiv(supportHash + i * i, storageSize)
        if currentTest == necessaryItem:
          pairs.append([curItem, necessaryItem])
          flag = True
          break
        else:
          i += 1
          currentTest = hashStorage[(hash + i * i) % storageSize]
      if flag:
        break
    if not flag:
      pairs.append([0, 0])
  return pairs

# Функция по созданию хэш-таблицы с разрешением коллизий
# по методу открытой адресации.
# Таблица использует двойное хеширование для пробирования
# Первая хеш-функция - функция по методу деления
# Вторая - комбинированая: сумма 1 и хеширования ключа по методу деления,
# причём ключ делится на storageSize - 1,
# где storageSize - размер внутренего хранилища хэш-таблицы
# Подсчитывание коллизий и поиск пар для сумм
def openAdressingDouble(array, summs, arraySize):
  colizionCount = 0
  storageSize = arraySize * 3
  hashStorage = [0] * storageSize
  for curItem in array:
    firstHash = hashFunctionDiv(curItem, storageSize)
    secondHash = hashFunctionDiv(curItem, storageSize - 1) + 1
    i = 0
    while True:
      hash = (firstHash + i * secondHash) % storageSize
      if hashStorage[hash]:
        colizionCount += 1
        i += 1
      else:
        hashStorage[hash] = curItem
        break
  pairs = [[colizionCount]]
  for curSumm in summs:
    flag = False
    for curItem in array:
      necessaryItem = curSumm - curItem
      firstHash = hashFunctionDiv(necessaryItem, storageSize)
      secondHash = hashFunctionDiv(necessaryItem, storageSize - 1) + 1
      i = 0
      currentTest = hashStorage[firstHash]
      while currentTest:
        hash = (firstHash + i * secondHash) % storageSize
        if currentTest == necessaryItem:
          pairs.append([curItem, necessaryItem])
          flag = True
          break
        else:
          i += 1
          currentTest = hashStorage[(firstHash + i * secondHash) % storageSize]
      if flag:
        break
    if not flag:
      pairs.append([0, 0])
  return pairs

# Набор функций:
functionCollector = [
  chainDiv,
  chainMult,
  openAdressingLinear,
  openAdressingQuadratic,
  openAdressingDouble
]

# Вызов необходимой функции:
output(functionCollector[numberHash - 1](array, summs, arraySize))
