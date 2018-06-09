from collections import namedtuple
from PIL import Image
import numpy as np
import math
fd = open("cow.obj")
vertex = []
triangles = []
for line in fd:
  if line[0] == 'v' and line[1] == ' ':
    vertex.append(list(map(lambda x: float(x), line[2::].split(' '))))
  if line[0] == 'f':
    triangles.append(list(map(lambda x: int(x.split('/')[0]) - 1, line[2::].split(' '))))

def area(A, B, C):
  a = math.sqrt((A[0]-B[0])*(A[0]-B[0]) + (A[1]-B[1])*(A[1]-B[1]) + (A[2]-B[2])*(A[2]-B[2]))
  b = math.sqrt((A[0]-C[0])*(A[0]-C[0]) + (A[1]-C[1])*(A[1]-C[1]) + (A[2]-C[2])*(A[2]-C[2]))
  c = math.sqrt((C[0]-B[0])*(C[0]-B[0]) + (C[1]-B[1])*(C[1]-B[1]) + (C[2]-B[2])*(C[2]-B[2]))
  p = (a+b+c) / 2
  return math.sqrt(p * (p-a) * (p-b) * (p-c))

for triangle in triangles:
  triangle[0] = vertex[triangle[0]]
  triangle[1] = vertex[triangle[1]]
  triangle[2] = vertex[triangle[2]]
  triangle.append([
    (triangle[0][0] + triangle[0][1] + triangle[0][2]) / 3,
    (triangle[1][0] + triangle[1][1] + triangle[1][2]) / 3,
    (triangle[2][0] + triangle[2][1] + triangle[2][2]) / 3
  ])
  triangle.append(area(triangle[0], triangle[1], triangle[2]))
print(triangles)
class nodeKD:
  left: None
  right: None
  median: None

class leafletKD():
  def __init__(self, triangle):
    self.triangle = triangle

def sortByFirst(element):
  return element[3][0]
def sortBySecond(element):
  return element[3][1]
def sortByThird(element):
  return element[3][2]

def makenodeKD(triangles, iteration):
  if iteration % 3 == 0:
    triangles.sort(key=sortByFirst)
  if iteration % 3 == 1:
    triangles.sort(key=sortBySecond)
  if iteration % 3 == 2:
    triangles.sort(key=sortByThird)
  if len(triangles) > 1:
    result = nodeKD()
    result.median = triangles[len(triangles) // 2]
    result.left = makenodeKD(triangles[0:len(triangles) // 2], iteration + 1)
    result.right = makenodeKD(triangles[len(triangles) // 2:len(triangles)], iteration + 1)
    return result
  if len(triangles) == 1:
    result = leafletKD(triangles[0])
    return result
  return None

root = makenodeKD(triangles, 0)
print(root.left.triangle)
print(root.median)
print(root.right.median)
print(root.right.left.triangle)
print(root.right.right.triangle)




############################

camera = [-2, 0, 0]
pictureCenter = [-1, 0, 0]
picture = []
for i in range(-100, 100):
  picture.append([])
  for j in range(-100, 100):
    if ()



# Coor = namedtuple('Coor', [0][1][2])


# print area(Coor(0, 0, 0), Coor(0, 0, 3), Coor(0, 4, 0))

def create_vector(A, B):
    return [B[0]-A[0], B[1]-A[1], B[2]-A[2]]

def vector_product(a, b):
  n = a[1]*b[2] - b[1]*a[2]
  m = a[2]*b[0] - b[2]*a[0]
  k = a[0]*b[1] - b[0]*a[1]
  VP = [n, m, k]
  return VP

def dot_product(a, b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

def normalize(a):
  ln = math.sqrt(a[0]*a[0] + a[1]*a[1] + a[2]*a[2])
  n = a[0] / ln
  m = a[1] / ln
  k = a[2] / ln
  norm = [n, m, k]
  return norm

def intersection(A, B, C, M, N):
  V1 =  vector_product(create_vector(A, B), create_vector(A, C))
  normV1 = normalize(V1)
  V2 = create_vector(M, A)
  d =  dot_product(normV1, V2)
  V3 = create_vector(M, N)
  e = dot_product(normV1, V3)
  if e == 0:
    return 0
  inter_x = M[0]  +  V3[0]*d/e
  inter_y = M[1]  +  V3[1]*d/e
  inter_z = M[2]  +  V3[2]*d/e
  inter = [inter_x, inter_y, inter_z]
  return abs(area(A, B, inter) + area(A, C, inter) + area(B, C, inter) - area(A, B, C)) < 1e-8

def convertToArray(pixels):
  return np.array(pixels, dtype = np.dtype('uint8'))

def writeToBMP(pixels, size, filename):
  array  = convertToArray(pixels)
  image = Image.Image()
  image = Image.fromarray(array, 'L')
  image.save(filename, 'BMP')
  return None