direcao = input().strip()

if direcao == "D":  # vai pra direita
    direcao = input().strip()
    if direcao == "D":  # ir pra direita novamente
        direcao = input().strip()
        if direcao == "C":
            print("E")
        elif direcao == "E":
            print("V")
        elif direcao == "D":
            print("X")
        elif direcao == "B":
            direcao = input().strip()
            if direcao == "E":
                print("P3")
            elif direcao == "B":
                print("P2")
            elif direcao == "D":
                print("P1")
            elif direcao == "C":
                print("V")
            else:
                print("E")
        else:
            print("E")
    elif direcao == "B":
        print("P3")
    elif direcao == "E":
        print("V")
    elif direcao == "C":
        print("E")
    else:
        print("E")
elif direcao == "E":
    print("E")
elif direcao == "C":
    print("E")
elif direcao == "B":
    print("X")
else:
    print("E")
