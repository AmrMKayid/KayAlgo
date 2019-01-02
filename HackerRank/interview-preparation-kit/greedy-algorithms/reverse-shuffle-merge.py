#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the reverseShuffleMerge function below.
def reverseShuffleMerge(s):
    from collections import defaultdict
    s = s[::-1]

    count = defaultdict(int)
    for c in s: count[c] += 1

    need = {}
    for c in count: need[c] = count[c] / 2

    solution = []
    i = 0
    while len(solution) < len(s) / 2:
        min_char_at = -1
        while True:
            c = s[i]
            if need[c] > 0 and (min_char_at < 0 or c < s[min_char_at]):
                min_char_at = i
            count[c] -= 1
            if count[c] < need[c]:
                break
            i += 1

        for j in range(min_char_at + 1, i + 1):
            count[s[j]] += 1
        need[s[min_char_at]] -= 1
        solution.append(s[min_char_at])
        i = min_char_at + 1

    return (''.join(solution))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = reverseShuffleMerge(s)

    fptr.write(result + '\n')

    fptr.close()
