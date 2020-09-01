#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
  colors = {}
  for i in ar:
    colors[i] = 0
  for i in ar:
    colors[i] += 1
  print(colors)
  pairs = 0
  for color in colors:
    pairs += colors[color] // 2
  return pairs


if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')

  n = int(input())

  ar = list(map(int, input().rstrip().split()))

  result = sockMerchant(n, ar)

  fptr.write(str(result) + '\n')

  fptr.close()
