# Input: arr[] = {1, 2, 4, 6, 3, 7, 8} ; n = 8
# Output: 5

# Input: arr[] = {1, 2, 3, 5}; n = 5
# Output: 4

from sum import missingNumberUsingSum
from xor import missingNumberUsingXOR


def missingNumber(arr, n):
    # return missingNumberUsingXOR(arr, n)
    return missingNumberUsingSum(arr, n)


arr = [1, 2, 4, 6, 3, 7, 8]
n = 8
print(missingNumber(arr, n))
