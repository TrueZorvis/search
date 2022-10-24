# Binary search requires that the array be sorted before the algorithm is executed.
# This makes the time complexity of binary search O(log n).

def binary_search(lys, val):
    first = 0
    last = len(lys)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid] == val:
            index = mid
        else:
            if val < lys[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return index


print(binary_search([10, 20, 30, 40, 50], 40))
