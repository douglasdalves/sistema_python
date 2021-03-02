import sys
from termcolor import colored

#--------------------------------------------
## configuracoes das mensagens


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(colored('ERRO: Por favor, digite um numero inteiro valido.','red'))
            continue
        except (KeyboardInterrupt):
            print(colored('Usuario preferiu nao digitar esse numero.','red'))
            return 0
        else:
            return n

def leia_opcao():
    print(colored('ERRO! Digite uma opcao valida!','magenta'))

#--------------------------------------------
#('Configuracoes do menu')

def linha(tam = 42):
    return '-' * tam

def cabeçalho (txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabeçalho('Testes secundários')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInt("\nSua Opção: ")
    return opc

#--------------------------------------------
#('Retornando para o menu principal')

def linha_igual(tam = 42):
    return '=' * tam

def retorno (txt):
    print(linha_igual())
    print(txt.center(42))
    print(linha_igual())
    print('\n')

def frase_retorno():
    retorno('Retornando para o menu principal')

#----------------------------------------