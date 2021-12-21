from Projeto.Crud.funcoes import *
from Projeto.Crud.interface import *
from Projeto.Crud.conexao import *


class Funcoes:
    def leiaInt(self, num):
        while True:
            try:
                n = int(input(num))
            except (ValueError, TypeError):
                print('\033[31mDigite um número inteiro válido\033[m')
                continue
            else:
                return n

    def visualizarTabela(self):
        cursor.execute('SELECT * FROM users')
        user = cursor.fetchall()
        linha()
        print(f'{"ID":^5}{"NOME":<10}{"SEXO":>5}{"IDADE":>10}{"PROFISSÃO":>15}')
        linha()
        for i in user:
            print(f'{i["id"]:^3}- {i["nome"]:<8}{i["sexo"]:>5}{i["idade"]:>10}{i["profissao"]:>18}')

    def visualizarUnico(self):
        while True:
            try:
                id = leiaInt('Digite o número ID: ')
                cursor = connection.cursor()
                cursor.execute(f'SELECT id, nome, sexo, idade, profissao from users where id = {id}')
                user = cursor.fetchall()
            except:
                print('\033[31mEste ID não esxiste na base de dados.\033[m')
                continue
            else:
                for i in user:
                    linha()
                    print(f'{"ID":^5}{"NOME":<10}{"SEXO":>5}{"IDADE":>10}{"PROFISSÃO":>15}')
                    linha()
                    print(f'{i[0]:^3}- {i[1]:<8}{i[2]:>5}{i[3]:>10}{i[4]:>18}')
                    break
            break

    def inserirDados(self, lista):
        while True:
            try:
                cursor.execute(f'INSERT INTO users(nome, sexo, idade, profissao) values ("{lista[0]}", "{lista[1]}", "{lista[2]}", "{lista[3]}")')
                connection.commit()
            except (ValueError, TypeError):
                print('\033[31mDados inválidos, tente novamente...\033[m')
                continue
            else:
                print('Dados inseridos com sucesso!!!')
                break

    def atualizarDados(self):
        try:
            id = leiaInt('Digite o ID para atualização: ')
            sexo = str(input('Digite o sexo: '))
            idade = leiaInt('Digite a nova idade: ')
            prof = str(input('Digite a nova profissão: '))
            cursor.execute(f'SELECT * FROM users WHERE id = {id}')
            user = cursor.fetchall()
            cursor.execute(f'UPDATE users SET sexo = "{sexo}", idade = {idade}, profissao = "{prof}" WHERE id = {id}')
            connection.commit()
        except:
            print('\033[31mERRO na atualização!\033[m')
        else:
            print('Dados atualizados com sucesso!')

    def apagarDados(self):
        while True:
            try:
                id = leiaInt('Deseja apagar os dados de qual ID: ')
                cursor.execute(f'SELECT * FROM users WHERE id = {id}')
                user = cursor.fetchall()
                cursor.execute(f'DELETE FROM users WHERE id = {id}')
                if user == '':
                    print('\033[1;31mNão existe cadastro com esse ID\033[m')
                    continue
            except:
                print('\033[1;31mOcorreu um ERRO ao apagar os dados!\033[m')
                break
            else:
                print('Dados apagado com sucesso!')
            break