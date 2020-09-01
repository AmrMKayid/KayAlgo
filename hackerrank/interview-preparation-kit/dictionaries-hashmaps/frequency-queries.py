#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the freqQuery function below.
def freqQuery(queries):
  from collections import defaultdict
  elementFreq = defaultdict(int)
  freqCount = defaultdict(int)
  ans = []
  for i, j in queries:
    if i == 1:
      if freqCount[elementFreq[j]]:
        freqCount[elementFreq[j]] -= 1
      elementFreq[j] += 1
      freqCount[elementFreq[j]] += 1
    elif i == 2:
      if elementFreq[j]:
        freqCount[elementFreq[j]] -= 1
        elementFreq[j] -= 1
        freqCount[elementFreq[j]] += 1
    else:
      if j in freqCount and freqCount[j]:
        ans.append(1)
      else:
        ans.append(0)
  return ans


if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')

  q = int(input().strip())

  queries = []

  for _ in range(q):
    queries.append(list(map(int, input().rstrip().split())))

  ans = freqQuery(queries)

  fptr.write('\n'.join(map(str, ans)))
  fptr.write('\n')

  fptr.close()
