import CalculatingWithFunctions as calc

def test_one():
    assert calc.seven(calc.times(calc.five())) ==  35
def test_two():
    assert calc.four(calc.plus(calc.nine())) ==  13
def test_drei():
    assert calc.eight(calc.minus(calc.three())) == 5
def test_four():
    assert calc.six(calc.divided_by(calc.two())) == 3