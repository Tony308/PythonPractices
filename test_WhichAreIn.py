import WhichAreIn

def test_one():
    a1 = ["live", "arp", "strong"] 
    a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
    r = ['arp', 'live', 'strong']
    assert WhichAreIn.in_array(a1, a2) == r

def test_two():
    a1 = ["tarp", "mice", "bull"]
    a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
    r = []
    assert WhichAreIn.in_array(a1, a2) == r
    
# def test_drei():
# def test_vier():