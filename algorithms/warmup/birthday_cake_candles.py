#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    return sum(i==ar[-1] for i in ar)

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, sorted(ar))
print(result)
