print('Введите название файла:')
fd = open(input(), 'r')
first = fd.readline().split(' ')
capacity = int(first[0])
count = int(first[1])
items = list(map(
  lambda x: list(map(
    lambda y: int(y), x.split(' ')
  )), fd
))
fd.close()

def sortByWeight(listElement):
  return listElement[1]
def sortByWeight2(listElement):
  return listElement[0]
items.sort(key = sortByWeight)

# print(items)


# # 

def knapsackOptimize(capacity, count, items):
  changesResonance1 = {
    0: 0,
  }
  # changesResonance2 = {}
  curItemIndex = -1
  for curItem in items:
    newChangesResonance = {}
    curItemIndex += 1
    # print(curItemIndex, curItem)
    # if curItemIndex % 2 == 0:
    for curOldChange in changesResonance1.items():
      # changesResonance2[curOldChange[0]] = curOldChange[1]
      if curItem[1] + curOldChange[0] > capacity:
        continue
      newChangesResonance[curItem[1] + curOldChange[0]] = curItem[0] + curOldChange[1]
      # print(newChangesResonance)
    # print('delStart')
    for i in newChangesResonance.items():
      # print(changesResonance1)
      if (i[0] in changesResonance1) and (changesResonance1[i[0]] >= i[1]):
        continue
      changesResonance1[i[0]] = i[1]
    # print('start')
    array = list(changesResonance1.items())
    array.sort(key = sortByWeight2)
    # print(array)
    print(array)
    for i in range(array.index(items[curItemIndex][1]), len(array) - 1):
      if array[i][1] >= array[i + 1][1]:
        # print(array[i], array[i + 1])
        # print(array[i + 1][0])
        del changesResonance1[array[i + 1][0]]
    # print(changesResonance1)
    # print('end')
      # for i in array.slice(0:-1):
      # if 
    # forDeleteOld = []
    # forDeleteNew = []
    # for curOldChange in changesResonance1.items():
    #   for curNewChange in newChangesResonance.items():
    #     if (curNewChange[0] <= curOldChange[0]) and (curNewChange[1] >= curOldChange[1]) and not (curOldChange[0] in forDeleteOld):
    #       forDeleteOld.append(curOldChange[0])
    #       break
    #     if curNewChange[0] > curOldChange[0] and curNewChange[1] < curOldChange[1] and not curNewChange[0] in forDeleteNew:
    #       # print('SMOTRI:', curNewChange, curOldChange)
    #       # print('EXTRAA')
    #       forDeleteNew.append(curNewChange[0])
    # print('delStartO')
    # for i in forDeleteOld:
    #   del changesResonance1[i]
    #   # del changesResonance2[i]
    # for i in forDeleteNew:
    #   del newChangesResonance[i]
    # for i in newChangesResonance.items():
    #   changesResonance1[i[0]] = i[1]
    # print('delFinish')
      
#       # OTL:

    # else:
    #   for curOldChange in changesResonance2.items():
    #     changesResonance1[curOldChange[0]] = curOldChange[1]
    #     if curItem[1] + curOldChange[0] > capacity:
    #       continue
    #     newChangesResonance[curItem[1] + curOldChange[0]] = curItem[0] + curOldChange[1]
    #   forDeleteOld = []
    #   forDeleteNew = []
    #   for curOldChange in changesResonance2.items():
    #     for curNewChange in newChangesResonance.items():
    #       if curNewChange[0] <= curOldChange[0] and curNewChange[1] >= curOldChange[1] and not curOldChange[0] in forDeleteOld:
    #         forDeleteOld.append(curOldChange[0])
    #         break
    #       if curNewChange[0] > curOldChange[0] and curNewChange[1] < curOldChange[1] and not curNewChange[0] in forDeleteNew:
    #         forDeleteNew.append(curNewChange[0])
    #   for i in forDeleteOld:
    #     del changesResonance1[i]
    #     del changesResonance2[i]
    #   for i in forDeleteNew:
    #     del newChangesResonance[i]

    #   for i in newChangesResonance.items():
    #     changesResonance1[i[0]] = i[1]
    # if curItemIndex == count - 1:
    # print(changesResonance1)
    # print(changesResonance2)
    if curItemIndex == count - 1:
      print('MAX:' + str(max(changesResonance1.values())))
    # print('MAX:' + str(max(changesResonance2.values())))

knapsackOptimize(capacity, count, items)
# # 

# def knapsack(capacity, count, items):
#   arr1 = [i for i in range(0, count + 1)]
#   arr2 = [i for i in range(0, count + 1)]
#   for itemIndex in range(0, count):
#     curItem = items[itemIndex]

#     if itemIndex % 2 == 0:
#       print(itemIndex)
#       for i in arr2.items():
#         print(i, curItem[1])
#         if (i[0] - curItem[1] < 0):
#           arr2[i[0]] = arr1[i[0]]
#           continue
#         arr2[i[0]] = max(i[1], arr1[i[0] - curItem[1]])
#     else:
#       print(itemIndex)
#       for i in arr1:
#         if (i[0] - curItem[1] < 0):
#           arr1[i[0]] = arr2[i[0]]
#           continue
#         arr1[i[0]] = max(i[1], arr2[i[0] - curItem[1]])

#     if itemIndex == 99:
#       print(arr2)


# knapsackOptimize(capacity, count, items)


# # def knapsack(prevOptArray, index):
# #   curOptArray = [0] * (capacity + 1)
# #   for i in range(0, capacity + 1):
# #     if i - items[index][1] < 0:
# #       curOptArray[i] = prevOptArray[i]
# #     else:
# #       curOptArray[i] = max([items[index][0] + prevOptArray[i - items[index][1]], prevOptArray[i]])
# #   print(curOptArray)
# #   if index < count - 1:
# #     return knapsack(curOptArray, index + 1)
# #   else:
# #     return curOptArray


# # print(knapsack([0] * (capacity + 1), 0)[capacity])

# # def knapsackOptimize(prevOptCollect, index):
# #   curValue = items[index][0]
# #   curWeight = items[index][1]
# #   сurOptCollect = prevOptCollect
# #   for key in prevOptCollect:
# #     curOptArray[key + curWeight] = max([curValue + prevOptArray[key], ])


############################################### Лёша:

# import sys
# from time import time

# if len(sys.argv) < 2:
#     print('Please, enter input filename')
#     exit(1)

# filename = sys.argv[1]
# file = open(filename)

# input = [line.strip().split() for line in file]
# file.close()
# # items = list(map(
# #   lambda x: list(map(
# #     lambda y: int(y), x.split(' ')
# #   )), fd.read().split('\n')
# # ))
# # print(input)
# data = list(map(
#   lambda x: list(map(
#     lambda y: int(y), x
#   )), input
# ))

# W = data[0][0]
# n = 500
# del data[0]

# cache = {}
# def knapsackTD(l, w):
#     global cache, data, W

#     key = str([l, w])
#     if key in cache:
#         return cache[key]


#     if l == 0 or W == 0: return 0

#     vi = data[l - 1][0]
#     wi = data[l - 1][1]

#     if wi > w:
#         res = knapsackTD(l - 1, w)
#         cache[key] = res
#         return res
#     else:
#         res = max([knapsackTD(l - 1, w), knapsackTD(l - 1, w - wi) + vi])
#         cache[key] = res
#         return res


# opt = knapsackTD(len(data), W)

# output = open('ip71_rumiantsev_07_output.txt', 'w')
# output.write(str(opt))
