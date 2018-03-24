#!/bin/python3

import sys

def timeConversion(s):
    first, second = s.split(':', 1)
    if first == '12': first = '00'
    return "{}:{}".format(int(first)+12 if 'PM' in second else first, second.strip('APM'))

s = input().strip()
result = timeConversion(s)
print(result)
