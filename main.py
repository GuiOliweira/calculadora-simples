def Menu():
    while True:
        print("\nMENU\n1- Somar\n2- Subtrair\n3- Multiplicar\n4- Dividir\n5- Sair\n")
        escolha = int(input("Escolha uma das opções: "))
        if escolha == 1:
            Soma()
            break
        elif escolha == 2:
            # Subtrair()
            break
        elif escolha == 3:
            # Multiplicar()
            break
        elif escolha == 4:
            # Dividir()
            break
        elif escolha == 5:
            break
        else:
            print("\nOpção inválida, tente novamente...\n")


def Soma():
    n1 = int(input("Digite o primeiro numero: "))
    n2 = int(input("Digite o segundo numero: "))
    soma = n1 + n2

    print(f"\nA soma de {n1} + {n2} é: {soma}\n")

    while True:
        escolha = int(input("Deseja uma nova soma? (1-Sim 2-Não): "))
        if escolha == 1:
            Soma()
            break
        elif escolha == 2:
            Menu()
            break
        else:
            print("\nOpção inválida, tente novamente...\n")


Menu()
