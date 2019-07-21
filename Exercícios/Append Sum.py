def append_sum(lst):
  soma = lst[-2]+lst[-1]
  lst.append(soma)
  soma1 = lst[-2]+lst[-1]
  lst.append(soma1)
  soma2 = lst[-2]+lst[-1]
  lst.append(soma2)
  return lst

#The function should add the last two elements of lst together and append the result to lst. 
#It should do this process three times and then return lst.

print(append_sum([1, 1, 2]))