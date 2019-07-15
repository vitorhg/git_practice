def combine_sort(lst1, lst2):
  lst3 = lst1+lst2
  lst3.sort()
  combine_sort = lst3
  return combine_sort

print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))