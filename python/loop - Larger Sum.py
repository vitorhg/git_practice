# A function named larger_sum() that takes two lists of numbers as parameters named lst1 and lst2.
# The function should return the list whose elements sum to the greater number.
# If the sum of the elements of each list are equal, return lst1.


def larger_sum(lst1, lst2):
    sum1 = 0
    sum2 = 0
    for number in lst1:
        sum1 += number
    for number in lst2:
        sum2 += number
    if sum1 >= sum2:
        return lst1
    else:
        return lst2


print(larger_sum([1, 9, 5], [2, 3, 7]))
