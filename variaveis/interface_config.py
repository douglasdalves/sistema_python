import sys
import os
import subprocess
from termcolor import colored
from datetime import datetime
import platform
import getpass

import pyautogui
from time import sleep

#------------------------------------------------
# variaveis

espaco = print('\n')

myfile_saindo="C:/scripts/funcoes/saindo_sistema.py"
myfile_captura="C:/scripts/bkp_arquivos/print_sistema.png"
myfile_print="C:/scripts/automacao_sh/altera_print.sh"
myfile_bkp_pip="C:/scripts/bkp_arquivos/backupPIP_python.txt"

#--------------------------------------------
# variaveis das funcoes conexao

ping_seanet = '186.251.248.1'
ping_roteador = '192.168.8.1'
ping_tv = '192.168.8.103'

ping_alexa = '192.168.8.107'
ping_plug1 = '192.168.8.108'
ping_plug2 = '192.168.8.109'
ping_lampada = '192.168.8.110'

ping_acer = '192.168.8.101'
ping_not_mor = '192.168.8.102'
ping_pc = '192.168.8.106'

ping_mi9 = '192.168.8.104'
ping_mi8 = '192.168.8.105'


#--------------------------------------------
#('Configuracoes do menu funcoes')

def linha_func(tam = 42):
    return '-' * tam

def func_cabecalho (txt):
    print('\n')
    print(linha_func())
    print(txt.center(42))
    print(linha_func())

#--------------------------------------------
# configuracao dados da maquina

def dados_pc():
    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
    text_data = colored('Data e Hora do teste:', 'blue', attrs=['bold'])

    cpu = platform.node()
    text_cpu = colored('Equipamento do Teste:', 'blue', attrs=['bold'])

    user = getpass.getuser()
    text_user = colored('Usuario do Sistema:', 'blue', attrs=['bold'])

    print('\n')
    print('--------- Testes Concluidos ---------')
    print(f'{text_data} {data_e_hora_em_texto}')
    print(f'{text_cpu} {cpu}')
    print(f'{text_user} {user}')
    print('\n')



#-----------------------------------------------------

# anotacao da config de data e hora

#---%d - O dia do mês representado por um número decimal (de 01 a 31)
#---%m - O mês representado por um número decimal (de 01 a 12)
#---%Y - O ano representado por um número decimal incluindo o século
#---%H - A hora representada por um número decimal usando um relógio de 24 horas (de 00 a 23)
#---%M - O minuto representado por um número decimal (de 00 a 59)

#-----------------------------------------------------



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
            print(colored('Usuario preferiu não digitar esse numero.','red'))
            return 0
        else:
            return n

def leia_opcao():
    print(colored('ERRO! Digite uma opção valida!','magenta'))

#--------------------------------------------
## configuracoes das opcoes


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
#('Configuracoes do menu inicial')

def linha(tam = 42): ## usado por outros menus
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


#--------------------------------------------
#('Configuracoes dos menus secudarios')

def cabeçalho (txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu_secund(lista):
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

def retorno (txt):
    print(linha())
    print(txt.center(42))
    print(linha())
    print('\n')

def frase_retorno():
    os.system('cls') or None
    retorno('Retornando para o menu principal')
    exec(open("sistema.py").read())