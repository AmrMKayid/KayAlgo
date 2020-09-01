#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
  import string
  ALPHABET = string.ascii_lowercase
  signatures = {}

  for start in range(len(s)):
    for finish in range(start, len(s)):
      signature = [0] * len(ALPHABET)
      for letter in s[start:finish + 1]:
        signature[ord(letter) - ord(ALPHABET[0])] += 1
      signature = tuple(signature)
      signatures[signature] = signatures.get(signature, 0) + 1
  res = 0
  for count in signatures.values():
    res += count * (count - 1) / 2
  return int(res)


if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')

  q = int(input())

  for q_itr in range(q):
    s = input()

    result = sherlockAndAnagrams(s)

    fptr.write(str(result) + '\n')

  fptr.close()
