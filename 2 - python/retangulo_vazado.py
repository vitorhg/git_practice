x = int(input("Digite a largura: "))
y = int(input("Digite a altura: "))
i=0

while i < y:
    if not i or i == y - 1:
        print("#" * x, end="")
        print()
    else:
        print("#" + " " * (x - 2) + "#")
    i+=1
