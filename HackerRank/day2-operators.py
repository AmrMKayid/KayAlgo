#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
	print('The total meal cost is ' 
		+ str(round(meal_cost + 
			((tip_percent*meal_cost)/100) + 
			((tax_percent*meal_cost)/100))) 
		+ ' dollars.')
	
if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
