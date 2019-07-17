dog_breeds = ['bulldog', 'dalmation', 'shihtzu', 'poodle', 'collie']

index = 0
while index < len(dog_breeds):
  print(dog_breeds[index])
  index += 1
#imprime os nomes até atingir o tamanho da lista


all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

while len(students_in_poetry) < 6:
  student = all_students.pop()
  students_in_poetry.append(student)
  
print(students_in_poetry)

#You are adding students to a Poetry class, the size of which is capped at 6.
#While the length of the students_in_poetry list is less than 6,
#use .pop() to take a student off the all_students list and add it to the students_in_poetry list.


def control_loop(val):
    # Return False if val exceeds limit of 10
    if val >= 10:
        return False
    return True
limit = 1
while control_loop(limit):
    limit += 1
    print(limit)
# while com função que imprime os valores até 10 e pára quando atinge esse número