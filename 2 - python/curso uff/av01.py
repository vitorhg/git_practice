documento = int(input())
digito1 = documento // 10000
digito2 = (documento // 1000) % 10
digito3 = (documento // 100) % 10
digito4 = (documento % 100) // 10
digito5 = documento % 10


def regras():
    if (
        (len(str(documento)) == 5)  # regra 1
        and ((digito2 ** 4) % 3 == 0)  # regra 2
        and ((digito4 ** 4) % 3 == 0)  # regra 2
        and (digito3 != 1)  # regra 3
        and (digito3 != 0)  # regra 3
        and (digito3 + digito5 > 3)  # regra 4
        and (digito1 == 2 or digito1 == 5 or digito1 == 9)  # regra 5
    ):
        return True
    else:
        return False

#print(digito1)
#print(digito2)
#print(digito3)
#print(digito4)
#print(digito5)
print(regras())
