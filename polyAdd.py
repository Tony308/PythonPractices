#!/usr/bin/env python3
# return the sum of the two polynomials p1 and p2.  
def poly_add(p1, p2):
    p1Length = len(p1)
    p2Length = len(p2)

    if p1Length < 1 and p2Length < 1:
        return []
    elif p1Length < 1:
        return p2
    elif p2Length < 1:
        return p1

    if p1Length < p2Length:
        return poly_add(p2, p1)

    index = p2Length - 1
    p1[index] += p2[index]
    p2.pop(index)
    return poly_add(p1, p2)

poly_add([19, 49, 40, 86, 60],
[20, 38, 10, 91, 56, 60, 32, 67, 69, 72, 68, 98, 11])