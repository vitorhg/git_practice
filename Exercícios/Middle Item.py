def middle_element(lst):
  if len(lst) % 2 == 0:
    sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1]
    return sum / 2
  else:
    return lst[int(len(lst)/2)]

#The index of the middle element can be found by using len(lst)/2. 
#However, division results in a float, and indices must be integers. 
#You can cast that number to be an integer using int(len(lst)/2).

#For lists with an even number of indices, you will want the element at the index found above 
#and also the element at index int(len(lst)/2) - 1

print(middle_element([5, 2, -10, -4, 4, 5]))