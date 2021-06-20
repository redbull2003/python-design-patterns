"""
    Iterable, Iterator, Iteration => Iterate
"""

for i in range(1, 7):  # Iteration
    print(i)
# -----------------------------------------

nums = [1, 2, 7, 17] # Iterable obj => set, tuple, dict, strings

for num in nums: # Iteration
    print(num)
# -----------------------------------------

i_nums = iter(nums) # Iterator => keep the last state

print(dir(i_nums)) # properties and methods in (i_nums)

print(next(i_nums))
print(i_nums.__next__())
print(next(i_nums))