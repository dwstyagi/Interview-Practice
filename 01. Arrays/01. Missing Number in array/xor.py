def missingNumberUsingXOR(arr, n):

    xor_x1 = 0

    # XOR all the array elements,
    # result will be x1
    for i in arr:
        xor_x1 ^= i

    # XOR all numbers from 1 to n
    xor_x2 = 0
    for i in range(1, n + 1):
        xor_x2 ^= i

    return xor_x1 ^ xor_x2
