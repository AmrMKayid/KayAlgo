#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumBribes function below.
def minimumBribes(q):
  """
    2 1 5 3 4
    2 5 1 3 4
    """
  count = 0
  for i in range(len(q) - 1, -1, -1):
    # print(q)
    if q[i] != (i + 1):
      if (i - 1) >= 0 and q[i - 1] == (i + 1):
        q[i], q[i - 1] = q[i - 1], q[i]
        count += 1
      elif (i - 2) >= 0 and q[i - 2] == (i + 1):
        q[i - 2], q[i - 1], q[i] = q[i - 1], q[i], (i + 1)
        count += 2
      else:
        print('Too chaotic')
        return
  print(count)


if __name__ == '__main__':
  t = int(input())

  for t_itr in range(t):
    n = int(input())

    q = list(map(int, input().rstrip().split()))

    minimumBribes(q)
