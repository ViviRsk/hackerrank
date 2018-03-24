#!/bin/python3

import sys

def miniMaxSum(arr):
    print(sum(arr[:-1]), sum(arr[1:]))

if __name__ == "__main__":
    arr = sorted(list(map(int, input().strip().split(' '))))
    miniMaxSum(arr)
