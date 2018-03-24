#!/bin/python3

from collections import defaultdict
import sys

def plusMinus(arr):
    d = defaultdict(int)
    for item in arr:
        if item > 0:
            d['positive'] += 1
        elif item < 0:
            d['negative'] += 1
        else:
            d['zeroes'] += 1
    for type_ in ['positive', 'negative', 'zeroes']:
        print("{:.6f}".format(d[type_]/float(n)))

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    plusMinus(arr)
