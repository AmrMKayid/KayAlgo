#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countTriplets function below.
def countTriplets(arr, r):
  tripltes, left, right = 0, {}, {}
  for num in arr:
    right[num] = right.get(num, 0) + 1

  for i in range(len(arr)):
    right[arr[i]] -= 1
    if arr[i] % r == 0:
      try:
        tripltes += left[arr[i] / r] * right[arr[i] * r]
      except:
        tripltes += 0
    left[arr[i]] = left.get(arr[i], 0) + 1

  return tripltes


if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')

  nr = input().rstrip().split()

  n = int(nr[0])

  r = int(nr[1])

  arr = list(map(int, input().rstrip().split()))

  ans = countTriplets(arr, r)

  fptr.write(str(ans) + '\n')

  fptr.close()
