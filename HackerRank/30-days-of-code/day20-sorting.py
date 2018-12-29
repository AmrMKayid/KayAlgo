#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

total_swaps = 0
for i in range(n):
    num_of_swaps = 0
    for j in range(0, n - 1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            num_of_swaps += 1
            total_swaps += 1
            
    if num_of_swaps == 0:
        break


print('Array is sorted in {} swaps.'.format(total_swaps))
print('First Element: {}'.format(a[0]))
print('Last Element: {}'.format(a[n - 1]))

