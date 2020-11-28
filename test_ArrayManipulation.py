import ArrayManipulation as func


def test_one():
    assert func.arrayManipulation(5, [ [ 1, 2, 100 ], [ 2, 5, 100 ], [ 3, 4, 100 ] ]) == 200
def test_zwei():
    assert func.arrayManipulation(10, [[1, 5, 3],[4, 8, 7],[6, 9, 1]]) == 10
def test_drei():
    assert func.arrayManipulation(10,[[2, 6, 8],[3 ,5 ,7],[1 ,8, 1],[5, 9 ,15]]) == 31