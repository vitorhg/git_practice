def every_three_nums(start):
    return list(range(start, 101, 3))


# The function should return a list of every third number between start and 100 (inclusive).
# For example, every_three_nums(91) should return the list [91, 94, 97, 100].
# If start is greater than 100, the function should return an empty list.
# Use the range function with three parameters to generate your list.
# Remember, the first parameter is the starting point (inclusive).
# The second parameter is the ending point (exclusive).
# The third parameter is the step.
# Range returns a range object, so make sure to cast it as a list by using list(range(...)).

# https://discuss.codecademy.com/t/what-happens-if-the-step-parameter-of-the-range-function-is-very-large/377347

print(every_three_nums(91))
