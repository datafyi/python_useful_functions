import random

l = random.sample(range(20), 10)

n = len(l)

for i in range(n):
    pos = i
    for j in range(i + 1, n):
        if l[j] < l[pos]:
            pos = j
    l[i], l[pos] = l[pos], l[i]
print(l)
