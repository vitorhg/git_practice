num = int(input("Digite um número inteiro: "))
unidade = 0
soma = 0

while num > 0:
    unidade = num % 10
    soma += unidade
    num = num // 10

print(soma)

