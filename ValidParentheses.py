def valid_parentheses(string):
    print(string)
    length = len(string)
    if (length < 1): return True
    return string[0] == "(" and string[length-1] == ')'

print(valid_parentheses("hi(hi)()"))