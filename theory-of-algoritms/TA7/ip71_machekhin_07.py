print('Введите название файла:')
fdInput = open(input(), 'r')
first = fdInput.readline().split(' ')
capacity = int(first[0])
count = int(first[1])
items = list(map(
  lambda x: list(map(
    lambda y: int(y), x.split(' ')
  )), fdInput
))
fdInput.close()

def sortBySecond(listElement):
  return listElement[1]
def sortByFirst(listElement):
  return listElement[0]

items.sort(key = sortBySecond)

def knapsackOptimize(capacity, count, items):
  changesResonance = {
    0: 0, # weight: value
  }
  for curItem in items: # [value, weight]
    newChangesResonance = {}
    for curOldChange in changesResonance.items():
      if curItem[1] + curOldChange[0] > capacity:
        continue
      newChangesResonance[curItem[1] + curOldChange[0]] = curItem[0] + curOldChange[1]
    for newChange in newChangesResonance.items():
      if (newChange[0] in changesResonance) and (
        changesResonance[newChange[0]] >= newChange[1]
      ):
        continue
      changesResonance[newChange[0]] = newChange[1]
    array = list(changesResonance.items())
    array.sort(key = sortByFirst)
    for changeIbdex in range(0, len(array) - 1):
      if array[changeIbdex][1] >= array[changeIbdex + 1][1]:
        del changesResonance[array[changeIbdex + 1][0]]
  fdOutput = open('ip71_machekhin_07_output.txt', 'w')
  fdOutput.write(str(max(changesResonance.values())))
  fdOutput.close()

knapsackOptimize(capacity, count, items)
