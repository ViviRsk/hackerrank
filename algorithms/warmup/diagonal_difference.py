"""
Given a square matrix of size N x N, calculate the absolute difference between the sums of its diagonals.
"""

import sys

n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

c = b = 0
for i in range(n):
    c += a[i][i]
    b += a[i][n-1-i]
print(abs(c-b))
