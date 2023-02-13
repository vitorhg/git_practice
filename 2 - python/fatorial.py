num = int(input("Digite o valor de n: "))

fatorial = 1

if num > 0:
    while num > 1:
        fatorial = fatorial * num
        num = num - 1
    print(fatorial)
elif num == 0:
    print(fatorial)
else:
    print("Digite um número positivo.")
