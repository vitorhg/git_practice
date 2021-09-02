import math

#Faça um programa que informe a distância em quilômetros (float) de um raio para o observador.
 #   O observador deve informar o tempo (float, em segundos) transcorrido entre ver o raio e ouvir o trovão.
  #  Assuma que a velocidade do som é 340 m/s.

#Exemplo:
#Entrada: 3
#Saída: 1.02

distanciakm = float(input())
distanciam = distanciakm * 1000
velocidade = 340
temposegundos = (distanciam * velocidade)/1000000

print(temposegundos)
