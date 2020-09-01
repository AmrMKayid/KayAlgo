#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the hourglassSum function below.
def hourglassSum(arr):
  """
    -9 -9 -9  1 1 1 
    0 -9  0  4 3 2
    -9 -9 -9  1 2 3
    0  0  8  6 6 0
    0  0  0 -2 0 0
    0  0  1  2 4 0
    """
  hourglass = []
  for row in range(4):
    for column in range(4):
      hourglass_arr = arr[row][column:column + 3] + arr[
          row + 1][column:column + 3] + arr[row + 2][column:column + 3]
      # print(hourglass_arr)
      hourglass.append(sum(hourglass_arr) - hourglass_arr[3] - hourglass_arr[5])
  return max(hourglass)


if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')

  arr = []

  for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

  result = hourglassSum(arr)

  fptr.write(str(result) + '\n')

  fptr.close()
