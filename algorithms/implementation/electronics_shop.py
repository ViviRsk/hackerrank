#!/bin/python3
"""
Monica wants to buy exactly one keyboard and one USB drive from her favorite
electronics store. The store sells n different brands of keyboards and m
different brands of USB drives. Monica has exactly s dollars to spend, and she
wants to spend as much of it as possible (i.e., the total cost of her purchase
must be maximal).

Given the price lists for the store's keyboards and USB drives, find and print
the amount of money Monica will spend. If she doesn't have enough money to buy
one keyboard and one USB drive, print -1 instead.
"""


def getMoneySpent(keyboards, drives, s):
    lst = max([i+j if i+j <= s else 0 for i in keyboards for j in drives])
    return lst if lst > 0 else -1


s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))
#  The maximum amount of money she can spend on a keyboard and USB drive, or
# -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)
