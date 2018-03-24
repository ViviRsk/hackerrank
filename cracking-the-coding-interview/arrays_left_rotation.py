#!/bin/python3

'''
Output Format

Print a single line of space-separated integers denoting the final state
of the array after performing left rotations.

Sample Input

5 4
1 2 3 4 5

Sample Output

5 1 2 3 4

Explanation

When we perform left rotations, the array undergoes the following sequence of
changes:

Thus, we print the array's final state as a single line of space-separated
values, which is 5 1 2 3 4.
'''


def array_left_rotation(a, n, k):
    return a[k:]+a[:k]


array_left_rotation(5, 3)
