
from termcolor import colored
from variaveis.interface_config import *


def sub_linha(tam = 42):
    return '-' * tam

def sub_cabecalho (txt):
    print('\n')
    print(sub_linha())
    print(txt.center(42))
    print(sub_linha())
    print('\n')


def wsl_status():
    sub_cabecalho('Dados dos Subsistemas')
    subprocess.run(["wsl", "-l", "-v"])
    print('\n')


def wsl_menu():
    aplicar = 0
    while aplicar != 5:
        print('''Opcoes:
        [1] Voltar ao menu
        [2] Start do Subsistema
        [3] Dados WSL
        [4] Dados Docker
        [5] Dados Vagrant''')
        print('\n')
        aplicar = str(input('Digite uma opcao? '))
        if aplicar == '1':
            sub_cabecalho('Tudo bem volte quando quiser')
            break
        if aplicar == '2':
            os.system('Ubuntu')
        if aplicar == '3':
            print('')
        if aplicar == '4':
            print('')
        else:
            aplicar == '5'




 