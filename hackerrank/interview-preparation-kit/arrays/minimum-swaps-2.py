#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumSwaps function below.
def minimumSwaps(arr):
  """
    1 3 5 2 4 6 7 <=
    1 5 3 2 4 6 7 
    1 4 3 2 5 6 7
    1 2 3 4 5 6 7
    """
  swap, i = 0, 0
  while i < len(arr):
    if arr[i] == (i + 1):
      i += 1
      continue
    arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]
    swap += 1
  return swap


if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')

  n = int(input())

  arr = list(map(int, input().rstrip().split()))

  res = minimumSwaps(arr)

  fptr.write(str(res) + '\n')

  fptr.close()
