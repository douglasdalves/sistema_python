import sys
import os
import pyautogui
from termcolor import colored
from time import sleep
import subprocess

#--------------------------------------------
## configuracoes das mensagens

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(colored('ERRO: Por favor, digite um número inteiro válido.','red'))
            continue
        except (KeyboardInterrupt):
            print(colored('Usuário preferiu não digitar esse número.','red'))
            return 0
        else:
            return n

def leia_opcao():
    print(colored('ERRO! Digite uma opção válida!','magenta'))

#--------------------------------------------
## configuracoes das opcoes

myfile_saindo="C:/scripts/funcoes/saindo_sistema.py"
myfile_captura="C:/scripts/bkp_arquivos/print_sistema.png"
myfile_print="C:/scripts/automacao_sh/altera_print.sh"


def gerar_print():
    print('\n')
    print('Opção 6 - Captura de Tela')
    print('Print gerado em bkp_arquivos')
    print('\n')
    capturar = pyautogui.screenshot()
    capturar.save(myfile_captura)
    subprocess.run(myfile_print, shell=True)

def funcao_sair():
    print('\n')
    cabecalho_sup('Saindo do sistema... Até logo')
    print('\n')
    sleep(2)
    exec(open(myfile_saindo).read())

#--------------------------------------------
#('Configuracoes do menu')

def linha(tam = 42):
    return '-' * tam

def cabecalho_sup (txt):
    print(linha())
    print(txt.center(55))
    print(linha())

def cabecalho_inf (txt):
    print(linha())
    print(txt.center(50))

def menu(lista):
    cabecalho_sup(colored('MENU PRINCIPAL','cyan',attrs=['bold']))
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    cabecalho_inf(colored('Escolha uma Opção','green'))
    print(linha())
    opc = leiaInt("\nSua Opção: ")
    return opc

#cabecalho_sup(colored('MENU PRINCIPAL','cyan',attrs=['bold']))
#cabecalho_sup('MENU PRINCIPAL')
