#!/bin/python3
"""
Gary is an avid hiker. He tracks his hikes meticulously, paying close
attention to small details like topography. During his last hike, he took
exactly n steps. For every step he took, he noted if it was an uphill or a
downhill step. Gary's hikes start and end at sea level. We define the
following terms:

-   A mountain is a non-empty sequence of consecutive steps above sea level,
    starting with a step up from sea level and ending with a step down to sea
    level.
-   A valley is a non-empty sequence of consecutive steps below sea level,
    starting with a step down from sea level and ending with a step up to sea
    level.

Given Gary's sequence of up and down steps during his last hike, find and 
print the number of valleys he walked through.
"""


def countingValleys(n, s):
    lst = [1 if i == 'U' else -1 for i in s]
    height = count = 0
    d = {}
    for j in range(n):
        height += lst[j]
        d[j] = height
        if height == 0 and j-1 in d and d[j-1] == -1:
            count += 1
    return count


if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    result = countingValleys(n, s)
    print(result)
