"""
    Shallow Copy vs Deep Copy
        only for mutable objects => (list, dict, set)
"""
import copy

# Shallow Copy
a = [1, 2, 3, 4]

# b = a
b = copy.copy(a)

b[0] = 7

print(a)
print(b)


# Deep Copy
a1 = [1, 2, 3, 4, [5, 6]]

# b = list(a)
b1 = copy.deepcopy(a1)

b1[4][0] = 7

print(a1)
print(b1)
