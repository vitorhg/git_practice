# cria uma lista de numeros e imprime
single_digits = list(range(10))
print(single_digits)
# imprime cada item individualmente
for i in single_digits:
    print(i)


# cria uma lista com o quadrado de cada item
squares = [x ** 2 for x in single_digits]
print(squares)


# cria uma lista com o cubo de cada item
cubes = [y ** 3 for y in single_digits]
print(cubes)
