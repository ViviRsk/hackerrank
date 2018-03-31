#!/bin/python3

"""
Anna and Brian order n items at a restaurant, but Anna declines to eat any of
the kth item due to an allergy. When the check comes, they decide to split the
cost of all the items they shared; however, Brian may have forgotten that they
didn't split the kth item and accidentally charged Anna for it.

You are given n, k, the cost of each of the n items, and the total amount of
money that Brian charged Anna for her portion of the bill. If the bill is
fairly split, print Bon Appetit; otherwise, print the amount of money that
Brian must refund to Anna. It is guaranteed that the amount will always be an
integer.
"""


def split_costs(k, price_list, charged):
    return "Bon Appetit" \
        if (sum(price_list) - price_list[k]) // 2 == charged \
        else price_list[k] // 2


n, k = input().split()
lst = [int(item) for item in input().split()]
charge = int(input())

print(split_costs(int(k), lst, charge))
