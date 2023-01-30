import random

l = random.sample(range(20), 10)
n = len(l)
print(l)

for i in range(1, n):
    pos = i
    for j in list(range(1, i + 1))[::-1]:
        if l[j] < l[j - 1]:
            l[j], l[j - 1] = l[j - 1], l[j]

print(l)
