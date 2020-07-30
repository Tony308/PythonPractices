def get_sum(a,b):
    ans = 0
    if a == b:
        return a
    elif b < a:
        return get_sum(b, a)
    for x in range(a,b+1):
        ans += x
    return ans