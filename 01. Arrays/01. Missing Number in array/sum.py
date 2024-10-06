# METHOD 2 (Use XOR)
#   1. XOR all the array elements, let the result of XOR be X1.
#   2. XOR all numbers from 1 to n, let XOR be X2.
#   3. XOR of X1 and X2 gives the missing number.


def missingNumberUsingSum(arr, n):
    # Calculate Sum
    total = (n * (n + 1)) // 2

    # subtract all number in array
    # to obtain a missing number
    for i in arr:
        total -= i

    return total
