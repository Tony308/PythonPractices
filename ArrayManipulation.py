#!/bin/python3
from collections import Counter
def arrayManipulation(n, queries):
    c = Counter()
    for start, end, summand in queries:
        c[start] += summand
        c[end+1] -= summand

    arrSum = 0
    highest = 0
    for i in sorted(c)[:-1]:
        arrSum += c[i]
        highest = max(highest, arrSum)
    return highest