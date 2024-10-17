from os import system
from time import sleep
from random import getrandbits


def function1():
    num = getrandbits(20)
    print("-------------------------------------------------")
    nome = str(input("Escreva o nome do contato: "))
    telefone = int(input("Escreva o teleforne do contato: +55(88)"))
    cpf = str(input("Escreva seu CPF: "))
    email = str(input("Escreva o e-mail do contato: "))
    print("\nSeu ID pessoal: {}".format(num))
    idContato = num

    try:

        agenda = open("agenda.txt", "a")
        dados = "Nome: {}; Telefone:+55(88){}; CPF: {}; E-mail: {}; ID_Pessoal: {}\n".format(
            nome, telefone, cpf, email, idContato)
        agenda.write(dados)
        agenda.close()
        print(f"\nContato salvo com Sucesso!")
        print("-------------------------------------------------")

    except:
        print("Erro na gravação dos Contatos")
        function1()
    while True:
        print(
            """
    SubMenu:

[1] para volta ao menu principal.
[2] Fecha Programa 

"""
        )
        volta = int(input("Digita a Opção: "))
        if volta >= 1 and volta <= 2:
            if volta == 1:
                system("cls" or "clear")
                menu()
                break
            elif volta == 2:
                system("cls" or "clear")
                print("\t>> Fechado Progrma <<")
                for i in range(9):
                    print(end="*" * i)
                    sleep(2)
                exit()
        else:
            system("cls" or "clear")
            print("\nOpção errada!")
        sleep(2)
        pass


def function2():
    system("cls" or "clear")
    print("\t\t>>> Registo dos Dados <<<\n")
    agenda = open("Agenda.txt", "r")
    for contato in agenda:
        print(contato)
    agenda.close()
    print("-" * 60)
    while True:
        print(
            """
    SubMenu:

[1] para volta ao menu principal.
[2] Fecha Programa 

"""
        )
        volta = int(input("Digita a Opção: "))
        if volta >= 1 and volta <= 2:
            if volta == 1:
                system("cls" or "clear")
                menu()
                break
            elif volta == 2:
                system("cls" or "clear")
                print("\t>> Fechado Progrma <<")
                for i in range(9):
                    print(end="*" * i)
                    sleep(2)
                exit()
        else:
            system("cls" or "clear")
            print("\nOpção errada!")
        sleep(2)
        pass


def function3():
    nomeDeletado = input("Digite o nome para ser deletado: ").lower()
    agenda = open("agenda.txt", "r")
    aux = []
    aux2 = []
    for i in agenda:
        aux.append(i)
    for i in range(0, len(aux)):
        if nomeDeletado not in aux[i].lower():
            aux2.append(aux[i])
    agenda = open("agenda.txt", "w")
    for i in aux2:
        agenda.write(i)
    print("Contato Deletado com Sucesso!")
    agenda.close()
    sleep(5)
    function2()


def function4():
    system("cls" or "clear")
    nome = str(input("Digita o nome: ")).upper()
    print(
        """
                 >> Registro <<
-------------------------------------------------"""
    )
    agenda = open("Agenda.txt", "r")

    for contato in agenda:
        if nome in contato.split(";")[1].upper():
            print(contato)
    agenda.close()
    while True:
        print(
            """
    SubMenu:
[1] para volta ao menu principal.
[2] Fecha Programa 

    """
        )
        volta = int(input("Digita a Opção: "))
        if volta >= 1 and volta <= 2:
            if volta == 1:
                system("cls" or "clear")
                menu()
                break
            elif volta == 2:
                system("cls" or "clear")
                print("\t>> Fechado Progrma <<")
                for i in range(9):
                    print(end="*" * i)
                    sleep(2)
                exit()
        else:
            system("cls" or "clear")
            print("\nOpção errada!")
        sleep(2)
        pass


def menu():
    while True:
        print(
            """
    |=============================================================================|
    |                       > PROJETO DE AGENDA DE CONTATOS <                     |
    |                                                                             |  
    |   Menu:                                                                     | 
    |                                                                             |  
    | [1] Cadastra Contato.                                                       | 
    | [2] Lista Contato.                                                          |
    | [3] Delete Contato.                                                         |
    | [4] Busca Contato pelo nome.                                                |
    | [5] Sair do Progrma.                                                        |
    |=============================================================================|"""
        )

        opcao = int(input("Escolha a Opção: "))

        if opcao >= 1 and opcao <= 5:
            if opcao == 1:
                function1()
                break
            elif opcao == 2:
                function2()
                break
            elif opcao == 3:
                function3()
                break
            elif opcao == 4:
                function4()
                break
            else:
                system("cls" or "clear")
                print("\t>> Fechado Progrma <<")
                for i in range(9):
                    print(end="*" * i)
                    sleep(2)
                exit()

        else:
            print("Opção errada!")
            sleep(2)
        pass


menu()
