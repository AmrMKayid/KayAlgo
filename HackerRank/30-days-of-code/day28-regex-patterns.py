#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())

    names = []
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        p = re.compile('^([a-zA-Z0-9_\-\.]+)@(gmail)\.(com)$')

        if p.match(emailID):
            names.append(firstName)
    
    for name in sorted(names):
        print(name)