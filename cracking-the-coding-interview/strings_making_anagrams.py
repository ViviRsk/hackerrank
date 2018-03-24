#!/bin/python

"""
Alice is taking a cryptography class and finding anagrams to be very useful.
We consider two strings to be anagrams of each other if the first string's
letters can be rearranged to form the second string.
In other words, both strings must contain the same exact letters in the same
exact frequency For example, bacdc and dcbac are anagrams, but bacdc and dcbad
are not.

Alice decides on an encryption scheme involving two large strings where
encryption is dependent on the minimum number of character deletions required
to make the two strings anagrams. Can you help her find this number?

Given two strings, and , that may or may not be of the same length, determine
the minimum number of character deletions required to make and anagrams.
Any characters can be deleted from either of the strings.

Input Format

The first line contains a single string, a.
The second line contains a single string, b.

Constraints

It is guaranteed that a and b consist of lowercase English alphabetic letters
(i.e., a through z).

Output Format

Print a single integer denoting the number of characters you must delete to
make the two strings anagrams of each other.

Sample Input

cde
abc

Sample Output

4

Explanation

We delete the following characters from our two strings to turn them into
anagrams of each other:

    Remove d and e from cde to get c.
    Remove a and b from abc to get c.

We must delete characters to make both strings anagrams, so we print on a new
line.
"""
from collections import Counter
import itertools


# ============================================================================
# Solution 1
# ============================================================================
def number_needed(a, b):
    count_a = Counter(a)
    count_b = Counter(b)
    count_a.subtract(count_b)
    return sum(abs(i) for i in count_a.values())


# ============================================================================
# Solution 2
# ============================================================================
def number_needed2(a, b):
    count = 0
    for i in range(97, 123):
        ia = sum(letter == chr(i) for letter in a)
        ib = sum(letter == chr(i) for letter in b)
        count += abs(ia - ib)
    return count


# ============================================================================
# Solution 3
# ============================================================================
# TODO: not working yet
def number_needed3(a, b):
    count = 0
    for i in range(97, 123):
        ia = len([i for i in itertools.ifilter(lambda x: x == chr(i), a)])
        ib = len([i for i in itertools.ifilter(lambda x: x == chr(i), b)])
        count += abs(ia - ib)
    return count


# ============================================================================
# Solution 4
# ============================================================================
def number_needed4(a, b):
    a = Counter(a)
    b = Counter(b)
    c = a - b
    d = b - a
    e = c + d
    return len(list(e.elements()))


a = 'bacdc'
b = 'dcbac'

# a = raw_input().strip()
# b = raw_input().strip()

print number_needed3(a, b)
