#!/bin/python3
"""
Brie’s Drawing teacher asks her class to open their n-page book to page number
p. Brie can either start turning pages from the front of the book (i.e., page
number 1) or from the back of the book (i.e., page number n), and she always
turns pages one-by-one (as opposed to skipping through multiple pages at
once). When she opens the book, page 1 is always on the right side.

Each page in the book has two sides, front and back, except for the last page
which may only have a front side depending on the total number of pages of the
book (see the Explanation sections below for additional diagrams).

Given n and p, find and print the minimum number of pages Brie must turn in
order to arrive at page p.

"""


def solve(n, p):
    n = (n + 1) if n % 2 == 0 else n
    return min(p // 2, (n - p) // 2)


n = int(input().strip())
p = int(input().strip())
result = solve(n, p)
print(result)
print(9//2)
