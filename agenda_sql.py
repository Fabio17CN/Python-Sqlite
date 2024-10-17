import sqlite3
from os import system
from time import sleep

#|-------------------------------------------------------------------------------------|#
#| Autor: Fabio da Costa Nascimento                                                    |#
#| Professor: Everton                                                                  |#
#| Cursor: Python                                                                      |#
#| Instituto: UTD - Secretaria da Ciêcia, Tecnologia e Educação Superior. Ceará        |#
#| Data: 16/01/2021                                                                    |#
#| Descrição: Projeto e basiado numa agenda telefonica,                                |#
#| aonde foi construindo usando linguagem de programação (Python e SQlite).            |#
#| a estrututa SQlite amazena os dados no banco de dados, aonde posso gerenciar        |#
#| varios dados e Salva, assim meus dados não se pederam,e meu conteudo ficaram salvo. |#
#|-------------------------------------------------------------------------------------|#


# -------Função Adicionar contatos
def adicionar():
    print('''\t>> ADICIONAR CONTATO <<<
 -----------------------------------------''')
    nome = input('Digita seu Nome: ')
    telefone = input("Digita Seu Telefone: ")
    email = input("Digita seu E-mail: ")
    cpf = input("Digita seu CPF: ")
    edereco = input("Digita seu Cidade: ")
    cursor.execute(
        f"INSERT INTO dados(nome, telefone, email,cpf,edereco)VALUES('{nome}','{telefone}','{email}','{cpf}','{edereco}');")
    conexao.commit()
    print("--------------------------------------------")
    print("Os Dados foram Adicionados Corretamente!")
    sleep(5)


# -----Função Ver Registro
def ver_registro():
    print('''\t>> Registro de Contatos <<<
-----------------------------------------''')
    cursor.execute("SELECT * FROM dados;")
    resultado = cursor.fetchall()
    for i in resultado:
        print('''
        Nome: %s 
        Telefône: %s
        E-mail: %s 
        CPF: %s 
        Edereço: %s
    ------------------------------''' % (i[0], i[1], i[2], i[3], i[4]))
    input("Presione qualquer tecla pra continua....")


# ------Função Buscar contato
def buscar():
    print('''\t>> Buscar Contatos <<<
-----------------------------------------''')
    buscar = input("Nome do contato: ")
    cursor.execute(f"SELECT * FROM dados WHERE nome = '{buscar}';")
    x = cursor.fetchall()
    for i in x:
        print('''
      Nome: {}
      Telefône:{}
      E-mail: {}
      CPF: {}
      Edereço: {}
      '''.format(i[0], i[1], i[2], i[3], i[4]))
    input("Presione qualquer tecla pra continua....")


# ----Função de Eliminar
def eliminar():
    print('''\t>> Eliminar Contato <<<
  -----------------------------------------''')
    eliminar = input("Nome do contato: ")
    cursor.execute(f"DELETE FROM dados WHERE nome= '{eliminar}';")
    conexao.commit()
    print("---------------------------------------------")
    print("Contato Eliminado do Registro!")
    input("Presione qualquer tecla pra continua....")


# Conexão com SQLite banco de dados
conexao = sqlite3.connect("Agenda_Contatos.db")
cursor = conexao.cursor()

# criar tabela se ela não existir ela criar.
cursor.execute("""CREATE TABLE IF NOT EXISTS dados(
            nome VARCHAR(80) NOT NULL,
            telefone VARCHAR(15) NOT NULL UNIQUE, 
            email VARCHAR(80) NOT NULL UNIQUE, 
            cpf VARCHAR(15) NOT NULL UNIQUE,
            edereco VARCHAR(50) NOT NULL)
            """)

# ==============(Menu Pricipal)==========================

while True:
    system('cls' or 'clear')
    print('''
        > Registro de Contato < 
-------------------------------------------
menu:
[1] Adicionar Contato no Registro.
[2] Ver Contato do Registro. 
[3] Buscar contato Registro.
[4] Deletar um Registro
[5] Sair do programa.
''')
    opcion = int(input("Digita a Opção ->: "))
    if opcion >= 1 and opcion <= 5:
        if opcion == 1:
            system('cls' or 'clear')
            adicionar()
        elif opcion == 2:
            system('cls' or 'clear')
            ver_registro()
        elif opcion == 3:
            system('cls' or 'clear')
            buscar()
        elif opcion == 4:
            system('cls' or 'clear')
            eliminar()
        else:
            print("-------------------------------------------")
            print("\t>> Saindo do Programa <<<")
            for i in range(50):
                sleep(5)
                exit()
            break
    else:
        print("> Opção Invalida....")
        sleep(2)
conexao.close()
