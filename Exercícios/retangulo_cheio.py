x = int(input("Digite a largura: "))
y = int(input("Digite a altura: "))
i = 0

while i != y:
    j = 0
    while j != x:
        print("#", end="")
        j += 1
    print("")
    i += 1

