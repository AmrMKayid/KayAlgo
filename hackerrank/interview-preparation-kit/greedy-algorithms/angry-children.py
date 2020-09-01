#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the maxMin function below.
def maxMin(k, arr):
  arr = sorted(arr)
  # max_min = float('inf')
  # for i in range(len(arr)):
  #     subarr = arr[i:i+k]
  #     if len(subarr) != k:
  #         continue
  #     max_min = min(max_min, max(subarr) - min(subarr))
  # return max_min
  return min([abs(arr[i + k - 1] - arr[i]) for i in range(len(arr) - k + 1)])


if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')

  n = int(input())

  k = int(input())

  arr = []

  for _ in range(n):
    arr_item = int(input())
    arr.append(arr_item)

  result = maxMin(k, arr)

  fptr.write(str(result) + '\n')

  fptr.close()
