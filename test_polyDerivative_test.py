import PolyDerivative

def test_eins():
    assert PolyDerivative.poly_derivative([1, 2]) == [2]

def test_empty():
    assert PolyDerivative.poly_derivative([]) == []
    assert PolyDerivative.poly_derivative([43]) == []

def test_drei():
    assert PolyDerivative.poly_derivative([1,2,3]) == [2,6]
    assert PolyDerivative.poly_derivative([9, 1, 3]) == [1, 6]

def test_zwei():
    assert PolyDerivative.poly_derivative([85, 44]) == [44]

def test_random():
    assert PolyDerivative.poly_derivative([38, 90, 141, 264]) == [90, 282, 792]
    assert PolyDerivative.poly_derivative([16, 64, 3, 212, 65, 84, 154, 464, 252, 500, 264, 1140, 936, 238, 45, 224]) == [64, 6, 636, 260, 420, 924, 3248, 2016, 4500, 2640, 12540, 11232, 3094, 630, 3360]
    assert PolyDerivative.poly_derivative([63, 58, 27, 8, 305, 12, 364, 504, 747, 570] ) == [58, 54, 24, 1220, 60, 2184, 3528, 5976, 5130]
