#naõ consegui terminar a tempo :(
texto = str(input().strip()) #entrada do texto
textovirgula = texto.replace(",", "")
textoponto = textovirgula.replace(".", "")
texto1 = textoponto.replace(";", "")
textolista1 = texto1.split()
# print(texto1) #ok
lista = str(input().strip()) #entrada das palavras
lista1 = lista.split()
# print(lista1) #ok
numerodepalavras = int(len(texto1.split())) #quantidade de palavras
# print(numerodepalavras) #ok
palavra1 = lista1[0]
palavra2 = lista1[1]
# print(lista1[0], lista1[1])
# print(palavra1, palavra2) #ok
#contar ocorrencias
quantpalavra1 = int(texto1.find(str(palavra1))) #lista1.len(re.findall(palavra1, textolista1))count sum(palavra1 for palavra1 in texto1.split()) (palavra1)#
print(quantpalavra1)
quantpalavra2 = int(texto1.find(palavra2)) #int(texto1.find(palavra2))
#print(quantpalavra1, quantpalavra2)
porcentagem1 = int(quantpalavra1)/numerodepalavras
porcentagem2 = int(quantpalavra2)/numerodepalavras
#print(porcentagem1, porcentagem2)

#saídas
print(numerodepalavras)
print(palavra1, quantpalavra1)
print(palavra2, quantpalavra2)
# quantidade de vezes que as palavras informadas aparecem, verificar vazia,ou que aparece primeiro
if quantpalavra1 > quantpalavra2:
    print(f'{palavra1} {porcentagem1:.2f}%')
elif quantpalavra1 < quantpalavra2:
    print(f'{palavra2} {porcentagem2:.2f}%')
else:
    print()