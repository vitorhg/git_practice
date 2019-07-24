def append_size(lst):
    lst.append(len(lst))
    return lst


# The function should append the size of lst (inclusive) to the end of lst.
# The function should then return this new list.

print(append_size([23, 42, 108]))
