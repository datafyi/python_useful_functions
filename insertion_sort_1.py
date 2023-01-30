import random

l = random.sample(range(20), 10)
n = len(l)
print(l)

for i in range(1, n):
    j = i
    while j > 0 and l[j] < l[j - 1]:
        l[j], l[j - 1] = l[j - 1], l[j]
        j = j - 1

print(l)
