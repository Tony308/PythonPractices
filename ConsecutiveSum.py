import math
def consecutive_sum(num):
    if num == 1:
        return 1
    result = 1
    end = math.ceil(num/2)+1
    for x in range(2,end):
        sum = (x * (x + 1)) / 2
        if sum > num: break
        temp = num - sum
        result += (temp % x == 0 )
    return result