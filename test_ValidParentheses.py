import ValidParentheses as func

def test_eins():
    assert func.valid_parentheses("  (") == False
def test_two():
    assert func.valid_parentheses("hi(hi)()") == True
def test_drei():
    assert func.valid_parentheses(")test") == False
def test_vier():
    assert func.valid_parentheses("") == True
def test_funft():
    assert func.valid_parentheses("hi())(") == False
    