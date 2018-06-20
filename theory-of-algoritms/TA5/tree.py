



# print(tree.root)

# def treeMin(this):
#   curNode = this.root
#   if (not curNode):
#     return None
#   while (curNode.leftChild):
#     curNode = curNode.leftChild
#   return curNode.data

# def treeMax(this):
#   curNode = this.root
#   if (not curNode):
#     return None
#   while (curNode.rightChild):
#     curNode = curNode.rightChild
#   return curNode.data

# def treeMinDel(this):
#   this.countNodes -= 1
#   curNode = this.root
#   if (not curNode):
#     return None
#   if (not curNode.leftChild):
#     min = curNode.data
#     this.root = curNode.rightChild
#     return min
#   while (curNode.leftChild.leftChild):
#     curNode = curNode.leftChild
#   min = curNode.leftChild.data
#   curNode.leftChild = curNode.leftChild.rightChild
#   return min

# def treeMaxDel(this):
#   this.countNodes -= 1
#   curNode = this.root
#   if (not curNode):
#     return None
#   if (not curNode.rightChild):
#     max = curNode.data
#     this.root = curNode.leftChild
#     return max
#   while (curNode.rightChild.rightChild):
#     curNode = curNode.rightChild
#   max = curNode.rightChild.data
#   curNode.rightChild = curNode.rightChild.leftChild
#   return max

# def treeAdd(this, value):
#   this.countNodes += 1
#   if(not this.root):
#     this.root = TreeNode(value)
#     pass
#   curNode = this.root
#   while (True):
#     if (value < curNode.data):
#       if (curNode.leftChild):
#         curNode = curNode.leftChild
#       else:
#         curNode.leftChild = TreeNode(value)
#         break
#     else:
#       if (curNode.rightChild):
#         curNode = curNode.rightChild
#       else:
#         curNode.rightChild = TreeNode(value)
#         break
#   return this

# class Tree:
#   def __init__(this, *firstNode):
#     if (firstNode):
#       this.root = TreeNode(firstNode[0])
#       this.countNodes += 1
#   root = None
#   countNodes = 0
#   min = treeMin
#   max = treeMax
#   add = treeAdd
#   minDel = treeMinDel
#   maxDel = treeMaxDel

# class TreeNode:
#   def __init__(this, value):
#     this.data = value
#   leftChild = None
#   rightChild = None

# lowTree = Tree(min(arr[0], arr[1]))
# hightTree = Tree(max(arr[0], arr[1]))

# fd = open('ip71_machkhin_05output.txt', 'w')
# fd.write(str(arr[0]) + '\n')
# fd.write(str(arr[0]) + ' ' + str(arr[1]) + '\n')


# for curIndex in range(2, countElements):
#   curElement = arr[curIndex]
#   if (lowTree.max() > curElement):
#     lowTree.add(curElement)
#   else:
#     hightTree.add(curElement)
#   if (lowTree.countNodes - hightTree.countNodes > 1):
#     hightTree.add(lowTree.maxDel())
#   if (hightTree.countNodes - lowTree.countNodes > 1):
#     lowTree.add(hightTree.minDel())
#   if (curIndex % 2 == 0): 
#     if (lowTree.countNodes < hightTree.countNodes):
#       fd.write(str(hightTree.min()) + '\n')
#     else:
#       fd.write(str(lowTree.max()) + '\n')
#   else:
#     fd.write(str(lowTree.max()) + ' ' + str(hightTree.min()) + '\n')

# fd.close()
