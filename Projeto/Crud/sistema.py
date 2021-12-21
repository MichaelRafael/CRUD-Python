from Projeto.Crud.funcoes import *
from Projeto.Crud.interface import *
from time import sleep

cabecalho('SISTEMA DE BANCO DE DADOS')

while True:
    resposta = menu(['Visualizar dados', 'Visualizar dado específico', 'Inserir dados', 'Atualizar dados', 'Apagar dados', 'Sair do sistema'])
    if resposta == 1:
        cabecalho('VISUALIZAR DADOS')
        r1 = Funcoes()
        Funcoes.visualizarTabela(r1)
    elif resposta == 2:
        cabecalho('VISUALIZAR ÚNICO DADO')
        r2 = Funcoes()
        Funcoes.visualizarUnico(r2)
    elif resposta == 3:
        cabecalho('INSERIR DADOS')
        lista = []
        nome = str(input('Digite o nome: '))
        sexo = str(input('Digite o sexo: '))
        idade = leiaInt('Digite a idade: ')
        prof = str(input('Digite a profissão: '))
        lista.append(nome)
        lista.append(sexo)
        lista.append(idade)
        lista.append(prof)
        r3 = Funcoes()
        Funcoes.inserirDados(r3, lista)
    elif resposta == 4:
        cabecalho('ATUALIZAR DADOS')
        r4 = Funcoes()
        Funcoes.atualizarDados(r4)
    elif resposta == 5:
        cabecalho('APAGAR DADOS')
        r5 = Funcoes()
        Funcoes.apagarDados(r5)
    elif resposta == 6:
        cabecalho('SAINDO DAS FUNÇÕES... ATÉ LOGO!')
        break
    else:
        print('\033[31mDigite uma opção válida\033[m')
    sleep(2)
