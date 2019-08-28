import math

print("A equação está na forma ax² + bx + c")
a = int(input("Digite a: "))
b = int(input("Digite b: "))
c = int(input("Digite c: "))

delta = b ** 2 - 4 * a * c

if delta < 0:
    print("esta equação não possui raízes reais")
elif delta == 0:
    raiz0 = -b / 2 * a
    print(f"a raiz desta equação é {raiz0}")
else:
    raiz1 = (-b + math.sqrt(delta)) / 2 * a
    raiz2 = (-b - math.sqrt(delta)) / 2 * a
    if raiz1 < raiz2:
        print(f"as raízes da equação são {raiz1} e {raiz2}")
    else:
        print(f"as raízes da equação são {raiz2} e {raiz1}")
