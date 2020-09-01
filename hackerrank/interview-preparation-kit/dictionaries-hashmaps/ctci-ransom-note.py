#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
  mag_dic = {}
  for w in magazine:
    mag_dic[w] = 0
  for w in magazine:
    mag_dic[w] += 1

  for n in note:
    if n in mag_dic and mag_dic[n] > 0:
      mag_dic[n] -= 1
      continue
    else:
      print("No")
      return
  print("Yes")


if __name__ == '__main__':
  mn = input().split()

  m = int(mn[0])

  n = int(mn[1])

  magazine = input().rstrip().split()

  note = input().rstrip().split()

  checkMagazine(magazine, note)
