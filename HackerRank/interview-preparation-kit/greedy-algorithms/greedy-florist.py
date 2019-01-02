#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    min_cost, prev_cost = 0, 0
    c = sorted(c)[::-1]
    for i in range(1, len(c)+1):
        min_cost += (prev_cost + 1) * c[i-1]
        if i % k == 0:
            prev_cost += 1
    return min_cost
    # return sum([(i // k + 1) * cost for i, cost in enumerate(sorted(c, reverse=True))])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
