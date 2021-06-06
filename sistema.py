#------------------------------------------------
#Importacao de dados

from lib.interface import *
from comp_git.git_funcoes import *
from time import sleep
import os
import pyautogui
from termcolor import colored
import sys
import subprocess

#------------------------------------------------
#Linhas de personalizacao

#------------------------------------------------
#Funcoes atreladas

#------------------------------------------------
#Codigo do menu principal

while True:
    resposta = menu(['Testes de Conexao','Agilizando Tarefas','Test de Rede','Testes Automatizados','Testes de Monitoracao','Pull do GitHub','Captura de Tela','Sair'])
    if resposta == 1:
        print('Opção 1')
        os.system('cls') or None
        #os.system('test.bat')
        exec(open("./funcoes/conexao_seanet.py").read())
    elif resposta == 2:
        print('Opção 2')
        os.system('cls') or None
        exec(open("./lib/menu_tarefas.py").read())
    elif resposta == 3:
        print('Opção 3')
        os.system('cls') or None
        exec(open("./lib/menu_avancado.py").read())
    elif resposta == 4:
        print('Opção 4 - Validacao Automatizada')
        os.system('cls') or None
        exec(open("./lib/menu_automacao.py").read())
    elif resposta == 5:
        print('Opção 5 - Monitoracao da conexao')
        os.system('cls') or None
        exec(open("./lib/menu_aplicacao.py").read())
    elif resposta == 6:
        func_pull()
    elif resposta == 7:
        gerar_print()
    elif resposta == 8:
        funcao_sair()
    else:
        leia_opcao()
        sleep(2)
    

#sts = os.system("mycmd" + " myarg")
# becomes
#retcode = call("mycmd" + " myarg", shell=True)