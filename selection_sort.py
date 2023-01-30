import random

l = random.sample(range(20), 10)
print(l)
s1 = set(l)

# for i in range(len(l)):
#     # i = 0, 1, 2,...
#     swap_index,mini = i,l[i]
#     for j in range(i+1, len(l)):
#         if l[j] < mini:
#             mini = l[j]
#             swap_index = j
#     l[i],l[swap_index]=l[swap_index],l[i]

for i in range(len(l)):
    swap_index = i
    for j in range(i + 1, len(l)):
        if l[j] < l[swap_index]:
            swap_index = j
    l[i], l[swap_index] = l[swap_index], l[i]

s2 = set(l)
print(l)
print(s1 == s2)
