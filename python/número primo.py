num = int(input("Digite um número: "))

for i in range(2, num):
    if num % i == 0:
        print("não primo")
        break
else:
    print("primo")
