"""5.6. Looping Techniques

More info at:
https://docs.python.org/3/tutorial/datastructures.html#looping-techniques"""

import math

# Looping through dictionaries - key, value
knights = {'gallahad': 'the pure', 'robin': 'the brave'}

for k, v in knights.items():
    print(k, v)


# position index and corresponding value - enumerate()
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)


# Loop over two or more sequences - zip()
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))


# Loop over a sequence in reverse - reversed()
for i in reversed(range(1, 10, 2)):
    print(i)


# To loop over a sequence in sorted order - sorted()
# returns a new sorted list while leaving the source unaltered.
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)


## Eliminate duplicate elements - set()
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)


# Simpler and safer create a new list
# instead of change a list while you are looping over it
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []

for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print('Raw data:', *raw_data)
print('Filtered:', *filtered_data)
