#Entrada
dist_esperada = int(input().strip()) #distancia alvo em realacao ao solo, em km
quant_combust = int(input().strip()) #disponibilidade inicial, em kg

# iteração é feita 1 km por vez e terminar quando chegar em dist_esperada ou quando o combustível acabar
soma_pares = 0 # soma dos números inteiros pares menores que a distância atual, mais um
consumo = 0 # divisão da distância alvo por soma_pares

#saída
dist_atual = 0 #total ercorrido até o momento
combust_atual  = 0 # quntidade de combustivel disponivel ate o momento

while consumo < quant_combust or dist_atual == dist_esperada:
    if quant_combust <= 0:
        break
    #primeira etapa, soma dos pares
    x = 0
    y = dist_atual
    soma_pares = 0
    if( x % 2 != 0 ):
        x += 1
    while( x < y ):
        soma_pares = soma_pares + x
        x += 2
    soma_pares = soma_pares + 1
    #segunda etapa
    consumo = dist_esperada/soma_pares
    # atualização
    quant_combust = quant_combust - consumo
    dist_atual = dist_atual + 1
    print(int(dist_atual),int(quant_combust))
    if dist_atual == dist_esperada:
        break
    