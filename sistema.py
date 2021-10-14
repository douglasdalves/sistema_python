#------------------------------------------------
#Importacao de dados

from lib.menu_tarefas import abrir_taref
from lib.menu_avancado import abrir_avanc
from lib.menu_automacao import abrir_autom
from lib.menu_aplicacao import abrir_aplic
from lib.menu_wsl import abrir_wsl


from variaveis.interface_config import *
from time import sleep
import os
from termcolor import colored

from funcoes import *
from lib import *

#------------------------------------------------
#Codigo do menu principal

while True:
    resposta = menu(['Testes de Conexao','Agilizando Tarefas','Test de Rede','Testes Automatizados','Testes de Monitoracao','Tarefas em WSL','Pull do GitHub','Captura de Tela','Sair'])
    if resposta == 1:
        print('Opcao 1')
        os.system('cls') or None
        exec(open("./funcoes/conexao_seanet.py").read())
    elif resposta == 2:
        print('Opcao 2')
        os.system('cls') or None
        abrir_taref()
    elif resposta == 3:
        print('Opcao 3')
        os.system('cls') or None
        abrir_avanc()
    elif resposta == 4:
        print('Opcao 4 - Validacao Automatizada')
        os.system('cls') or None
        abrir_autom()
    elif resposta == 5:
        print('Opcao 5 - Monitoracao da conexao')
        os.system('cls') or None
        abrir_aplic()
    elif resposta == 6:
        print('Opcao 6')
        os.system('cls') or None
        abrir_wsl()
    elif resposta == 7:
        os.system('cp -r C:/scripts/comp_git/git_pull.py C:/scripts_logs')
        os.startfile('git_pull.py')
    elif resposta == 8:
        gerar_print()
    elif resposta == 9:
        funcao_sair()
    else:
        leia_opcao()
        sleep(2)
    

#sts = os.system("mycmd" + " myarg")
# becomes
#retcode = call("mycmd" + " myarg", shell=True)