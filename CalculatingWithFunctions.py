import operator
ops = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv} # etc.

def zero(*args):
    if (args):
        [args] = args
        [a,b] = args
        return int(ops[a](0,b))
    return 0

def one(*args):
    if (args):
        [args] = args
        [a,b] = args
        return int(ops[a](1,b))
    return 1

def two(*args):
    if (args):
        [args] = args
        [a,b] = args
        return int(ops[a](2,b))
         
    return 2

def three(*args):
    if (args):
        [args] = args
        [a,b] = args
        return int(ops[a](3,b))

    return 3

def four(*args):
    if (args):
        [args] = args
        [a,b] = args
        return int(ops[a](4,b))
         
    return 4

def five(*args):
    if (args):
        [args] = args
        [a,b] = args
        return int(ops[a](5,b))
         
    return 5

def six(*args):
    if (args):
        [args] = args
        [a,b] = args
        return int(ops[a](6,b))
    return 6

def seven(*args):
    if (args):
        [args] = args
        [a,b] = args
        return int(ops[a](7,b))
    return 7

def eight(*args):
    if (args):
        [args] = args
        [a,b] = args
        return int(ops[a](8,b))
    return 8

def nine(*args):
    if (args):
        [args] = args
        [a,b] = args
        return int(ops[a](9,b))
    return 9

def plus(num): 
    return ["+", num]
def minus(num): 
    return ["-", num]
def times(num): 
    return ["*", num]
def divided_by(num): 
    return ["/", num]