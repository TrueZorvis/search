# The time complexity of interpolation search is O(log log n) when values are uniformly distributed.
# If values are not uniformly distributed, the worst-case time complexity is O(n), the same as linear search.

def interpolation_search(lys, val):
    low = 0
    high = (len(lys) - 1)
    while low <= high and lys[low] <= val <= lys[high]:
        index = low + int(((float(high - low) / (lys[high] - lys[low])) * (val - lys[low])))
        if lys[index] == val:
            return index
        if lys[index] < val:
            low = index + 1
        else:
            high = index - 1
    return -1


print(interpolation_search([1, 2, 3, 4, 5, 6, 7, 8], 6))
