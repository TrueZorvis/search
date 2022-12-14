# It is also known by the names galloping search, doubling search and Struzik search.
# In its worst case, the time complexity is O(log n)

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


def exponential_search(lys, val):
    if lys[0] == val:
        return 0
    index = 1
    while index < len(lys) and lys[index] <= val:
        index = index * 2
    return binary_search(lys[:min(index, len(lys))], val)


print(exponential_search([1, 2, 3, 4, 5, 6, 7, 8], 5))
