#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the luckBalance function below.
def luckBalance(k, contests):
    important_contests = sorted([contest[0] for contest in contests if contest[1] == 1])[::-1]
    non_important_contests = [contest[0] for contest in contests if contest[1] == 0]
    # print(important_contests)
    # print(non_important_contests)
    luck = sum(non_important_contests)
    i = 0
    while k > 0:
        try:
            luck += important_contests[i]
        except:
            break
        i += 1
        k -= 1
    luck -= sum(important_contests[i:])
    return luck


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
