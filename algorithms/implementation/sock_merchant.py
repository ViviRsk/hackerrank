#!/bin/python3
"""
John works at a clothing store. He has a large pile of socks that he must pair
them by color for sale.

You will be given an array of integers representing the color of each sock.
Determine how many pairs of socks with matching colors there are.

John works at a clothing store and he's going through a pile of socks to find
the number of matching pairs. More specifically, he has a pile of n loose
socks where each sock i is labeled with an integer, ci, denoting its color. He
wants to sell as many socks as possible, but his customers will only buy them
in matching pairs. Two socks, i and j, are a single matching pair if they have
the same color (ci = cj).
"""


def sockMerchant(n, ar):
    pairs = 0
    stack = []
    for i in ar:
        if i in stack:
            stack.remove(i)
            pairs += 1
        else:
            stack.append(i)
    return pairs


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)
