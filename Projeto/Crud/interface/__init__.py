from Projeto.Crud.interface import *


def leiaInt(num):
    while True:
        try:
            n = int(input(num))
        except (ValueError, TypeError):
            print('\033[31mDigite um número inteiro válido\033[m')
            continue
        else:
            return n


def linha(tam=50):
    print(tam * '-')


def cabecalho(msg):
    linha()
    print(msg.center(50))
    linha()


def menu(lista):
    cabecalho('ESCOLHA UMA OPÇÃO')
    for p, i in enumerate(lista):
        print(f'\033[32m{p+1}\033[m - \033[34m{i}\033[m')
    linha()
    opc = leiaInt('\033[33mSua opção:\033[m ')
    return opc