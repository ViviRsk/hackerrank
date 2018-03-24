#!/bin/python3

"""
Alice and Bob each created one problem for HackerRank. A reviewer rates the 
two challenges, awarding points on a scale from 1 to 100 for three categories: 
problem clarity, originality, and difficulty.

We define the rating for Alice's challenge to be the triplet A = (a0,a1,a2), 
and the rating for Bob's challenge to be the triplet B = (b0,b1,b2).

Your task is to find their comparison points by comparing a0 with b0, a1 with 
b1, and a2 with b2.

- If ai > bi, then Alice is awarded 1 point.
- If ai < bi, then Bob is awarded 1 point.
- If ai = bi, then neither person receives a point.

Comparison points is the total points a person earned.

Given A and B, can you compare the two challenges and print their respective 
comparison points?
"""

import sys
from collections import Counter

def solve(a0, a1, a2, b0, b1, b2):
    # Complete this function
    a = Counter(a=a0, b=a1, c=a2)
    a.subtract(Counter(a=b0, b=b1, c=b2))
    return len([i for i in a.values() if i>0]), len([j for j in a.values() if j<0])

a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print (" ".join(map(str, result)))


# ============================================================================
# Solution 2
# ============================================================================
def solve2(a0, a1, a2, b0, b1, b2):
    a = (1 if a0 > b0 else 0) + (1 if a1 > b1 else 0) + (1 if a2 > b2 else 0)
    b = (1 if a0 < b0 else 0) + (1 if a1 < b1 else 0) + (1 if a2 < b2 else 0)
    return (a,b)

# ============================================================================
# Solution 3
# ============================================================================
def solve3(a0, a1, a2, b0, b1, b2):
    a = (a0 > b0) + (a1 > b1) + (a2 > b2)
    b = (a0 < b0) + (a1 < b1) + (a2 < b2)
    return (a,b)
    
# ============================================================================
# Solution 4
# ============================================================================
def solve4(a0, a1, a2, b0, b1, b2):
    Ascore = len([1 for a,b in zip(A,B) if a>b])
    # Ascore = sum(a>b for a, b in zip(A, B))
    Bscore = len([1 for a,b in zip(A,B) if b>a])
    return Ascore, Bscore

# ============================================================================
# Editorial
# ============================================================================
def solve5(a0, a1, a2, b0, b1, b2):
    a_triplet = a0, a1, a2
    b_triplet = b0, b1, b2
    alice_points = 0
    bob_points = 0
    for a_val, b_val in zip(a_triplet, b_triplet):
        if a_val < b_val:
            bob_points += 1
        elif a_val > b_val:
            alice_points += 1
    return (alice_points, bob_points)
