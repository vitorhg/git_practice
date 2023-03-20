def append_sum(lst):
    """
    Esta função adiciona três novos elementos à lista dada como entrada, calculando a soma dos dois últimos elementos da lista e adicionando esse resultado ao final da lista. O processo é repetido duas vezes mais.

    Parâmetros:
    lst (list): Lista a ser modificada.

    Retorna:
    list: Lista modificada com três novos elementos adicionados.

    Exemplo:
    >>> append_sum([1, 1, 2])
    [1, 1, 2, 2, 3, 5]
    """
    # calcula a soma dos dois últimos elementos da lista
    soma = lst[-2] + lst[-1]
    # adiciona a soma ao final da lista
    lst.append(soma)
    # calcula a soma dos dois últimos elementos da lista novamente
    soma1 = lst[-2] + lst[-1]
    # adiciona a soma ao final da lista novamente
    lst.append(soma1)
    # calcula a soma dos dois últimos elementos da lista novamente
    soma2 = lst[-2] + lst[-1]
    # adiciona a soma ao final da lista novamente
    lst.append(soma2)
    # retorna a lista modificada com os novos elementos adicionados
    return lst


print(append_sum([1, 1, 2]))
