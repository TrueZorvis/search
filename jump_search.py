# Jump search requires that the array be sorted before the algorithm is executed.
# The time complexity of jump search is O(sqrt(n))

import math


def jump_search(lys, val):
    length = len(lys)
    jump = int(math.sqrt(length))
    left, right = 0, 0
    while left < length and lys[left] <= val:
        right = min(length - 1, left + jump)
        if lys[left] <= val <= lys[right]:
            break
        left += jump
    if left >= length or lys[left] > val:
        return -1
    right = min(length - 1, right)
    i = left
    while i <= right and lys[i] <= val:
        if lys[i] == val:
            return i
        i += 1
    return -1


print(jump_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 5))
