def naiveSearch(L, e):
    for x in L:
        if x == e:
            return True

    return False


# print(naiveSearch([1,22,3,4,66,0,2], 989))

def binarySearch(L, e):
    tempL = L.copy()
    tempL.sort()
    left, right = 0, len(tempL) - 1
    while not left > right:
        mid = (left + right) // 2
        if tempL[mid] == e:
            return True
        elif tempL[mid] < e:
            left = mid + 1
        else:
            right = mid - 1

    return False


# print(binarySearch([1,2,34,5,6,78,9,0,-1],6))

def bSearch(v, L):
    if L == []:
        return False

    mid = len(L) // 2

    if L[mid] == v:
        return True

    if v < L[mid]:
        return bSearch(v, L[:mid])
    else:
        return bSearch(v, L[mid + 1:])


L1 = list(range(100))
L1.sort()
print(bSearch(12, L1))
