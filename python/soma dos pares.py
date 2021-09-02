'''s = 0
for c in range(1, 7):
    num = int(input('Digite um número inteiro: '))
    if num%2 == 0:
        s = s + num
print(f'A soma dos números pares informados é {s}.')


print(
    sum(
        [
            i
            for i in range(
                int(input("Informe o primeiro valor")),
                int(input("Informe o segundo valor")) + 1,
            )
            if i % 2 == 0
        ]
    )
)'''


x = int(input("digite um numero "))
y = int(input("digite um numero "))
soma = 0
if( x % 2 != 0 ):
  x += 1
while( x < y ):
  soma = soma + x
  x += 2
soma = soma + 1
print( soma )