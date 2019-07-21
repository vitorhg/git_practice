#The function should sum the elements of the list until the sum is greater than 9000. 
#When this happens, the function should return the sum. 
#If the sum of all of the elements is never greater than 9000, the function should return total sum of all the elements. 
#If the list is empty, the function should return 0.

def over_nine_thousand(lst):
  sum = 0
  for number in lst:
    sum += number
    if (sum > 9000):
      break
  return sum

print(over_nine_thousand([8000, 900, 120, 5000]))