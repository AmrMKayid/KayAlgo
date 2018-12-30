#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countingValleys function below.
def countingValleys(n, s):
    """
    UDDDUDUU
    DDUUDDUDUUUD
    """
    stack = []
    valleys, step = 0, 0
    while step < n:
        if len(stack) == 0 and s[step] == 'D':
            valleys += 1
        stack.append(s[step])
        step += 1
        while len(stack) != 0 and step < n:
            if stack[0] == s[step]:
                stack.append(s[step])
            else:
                stack.pop()
            step += 1
    return valleys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
