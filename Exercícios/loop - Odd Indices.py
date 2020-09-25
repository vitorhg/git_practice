# The function should create a new empty list and add every element from lst that has an odd index.
# The function should then return this new list.


def odd_indices(lst):
    new_lst = []
    for index in range(1, len(lst), 2):
        new_lst.append(lst[index])
    return new_lst


print(odd_indices([4, 3, 7, 10, 11, -2]))
