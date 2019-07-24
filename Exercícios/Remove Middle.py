# Write your function here
def remove_middle(lst, start, end):
    lst1 = lst[:start]
    lst2 = lst[end + 1 :]
    return lst1 + lst2


# Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))
