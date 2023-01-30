import random

l = random.sample(range(20), 10)
print(l)


def insert(L, v):
    if L == []:
        return [v]

    if v > L[-1]:
        return L + [v]
    else:
        return insert(L[:-1], v) + L[-1:]


def insertion_sort(L):
    if L == []:
        return L
    L = insert(insertion_sort(L[:-1]), L[-1])
    return L


print(insertion_sort(l))
