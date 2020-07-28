def poly_derivative(p):
    length = len(p)

    if length == 2:
        p.pop(0)
        return p
    elif length < 2:
        return []

    for i in range(2,length):
        p[i] *= i
    
    p.pop(0)
    print(p)
    return p
poly_derivative([62, 63, 29, 9, 2, 61, 2, 52, 63, 83, 57])