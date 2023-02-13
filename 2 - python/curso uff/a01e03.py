moedas = int(input())

moedas1real = moedas // 100
moedasrestantes1 = (moedas % 100)

moedas50cent = moedasrestantes1 // 50
moedasrestantes2 = moedasrestantes1 % 50

moedas25cent = moedasrestantes2 // 25
moedasrestantes3 = moedasrestantes2 % 25

moedas10cent = moedasrestantes3 // 10
moedasrestantes4 = moedasrestantes3 % 10

moedas5cent = moedasrestantes4 // 5
moedas1centavo = moedasrestantes4 % 5

print(moedas1real)
print(moedas50cent)
print(moedas25cent)
print(moedas10cent)
print(moedas5cent)
print(moedas1centavo)

#Faça um programa para, a partir de um valor informado em centavos, indicar a menor quantidade de moedas que representa esse valor.

#    Considere moedas de 1, 5, 10, 25 e 50 centavos, e 1 real.
 #   A saída deve ser a quantidade de cada moeda, uma por linha, em ordem decrescente de valor.

#Dicas:

 #   Para fazer uma divisão inteira em Python, use o operador //.
  #  Para descobrir o resto de uma divisão, use o operador %.

#Exemplo:

#Para uma entrada de 290 centavos, a menor quantidade de moedas é 2 moedas de 1 real, 1 moeda de 50 centavos, 1 moeda de 25 centavos, 1 moeda de 10 centavos, 1 moeda de 5 centavos e 0 moedas de 1 centavo.

#Entrada: 290

#Saída: 2 1 1 1 1 0
