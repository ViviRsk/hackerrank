#!/bin/python3

"""
A flock of n birds is flying across the continent. Each bird has a type, and the different types are designated 
by the ID numbers 1, 2, 3, 4, and 5. 
"""

import sys
from collections import Counter

def migratoryBirds(n, ar):
    counter = Counter(ar).most_common(1)[0][0]
    return counter

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)

# ar = [1, 4, 4, 4, 2, 2, 2, 5, 5, 5, 3]
