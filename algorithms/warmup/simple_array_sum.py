#!/bin/python

import sys

def simpleArraySum(n, ar):
    
    def add(num1,num2):
        return num1+num2
    return reduce(add, ar)

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = simpleArraySum(n, ar)
print(result)
