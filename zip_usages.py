# Read Blog  https://datascience.fyi/python-zip-function-usages-with-an-example.py

# python zip example
names = ['roza','sameer','sahadeba','sobhamayee']
food_preference = ['Chilly Chicken','Fruits','Fish','Chicken']

zip_object = zip(names,food_preference)
print(zip_object)
print(type(zip_object),' : ',(list(zip_object)))

# <zip object at 0x0000016FA77CDCC0>
# Output: <class 'zip'>  :  [('roza', 'Chilly Chicken'), ('sameer', 'Fruits'), ('sahadeba', 'Fish'), ('sobhamayee', 'Chicken')]

names = ['roza','sameer','sahadeba']
age = [26,31,66,61]

zip_object = zip(names,age)
print(list(zip_object))
# [('roza', 26), ('sameer', 31), ('sahadeba', 66)]

names = ['roza','sameer','sahadeba','sobhamayee']
age = [26,31,66]

zip_object = zip(names,age)
print(list(zip_object))
# [('roza', 26), ('sameer', 31), ('sahadeba', 66)]

from itertools import zip_longest

names = ['roza','sameer','sahadeba','sobhamayee']
age = [26,31,66]

zip_longest_object = zip_longest(names,age)
print(list(zip_longest_object))
# [('roza', 26), ('sameer', 31), ('sahadeba', 66), ('sobhamayee', None)]

