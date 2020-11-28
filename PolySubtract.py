def poly_subtract(p1, p2):
    p1Length = len(p1)
    p2Length = len(p2)

    if p1Length < 1 and p2Length < 1:
        return []
    elif p2Length < 1:
        return p1
    elif p1Length < 1:
        p1.append(0)
        return poly_subtract(p1,p2)
    elif p1Length < p2Length:
        p1.append(0)
        return poly_subtract(p1,p2)

    index = p2Length - 1
    p1[index] -= p2[index]
    p2.pop(index)
    return poly_subtract(p1, p2)