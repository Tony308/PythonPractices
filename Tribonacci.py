def tribonacci(signature, n):
    length = len(signature)
    if n <= length and n > 0:
        return signature[n-1]

    nextSum = tribonacci(signature, n-1) + tribonacci(signature, n-2) + tribonacci(signature, n-3)
    signature.append(nextSum)
    print(signature)
    return tribonacci(signature, n-1) + tribonacci(signature, n-2) + tribonacci(signature, n-3)
    
print("ans", tribonacci([1, 1, 1], 10))