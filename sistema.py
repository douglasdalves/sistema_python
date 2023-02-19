#------------------------------------------------
#Importacao de dados

from email.mime import application
from lib.menu_tarefas import abrir_taref
from lib.menu_avancado import abrir_avanc
from lib.menu_automacao import abrir_autom
from lib.menu_aplicacao import abrir_aplic
from lib.menu_wsl import abrir_wsl

from variaveis.interface_config import *
from time import sleep

from termcolor import colored
from funcoes import *
from lib import *

#------------------------------------------------
#

myfile_cp_logs = r'C:/scripts_logs'

# Dados menu em lista
mlist = ['Testes de Conexao', 'Agilizando Tarefas', 'Test de Rede', 'Testes Automatizados', 
'Testes de Monitoracao', 'Tarefas em WSL', 'Pull do GitHub','Web system', 'Captura de Tela', 'Sair']

#------------------------------------------------
#Codigo do menu principal


while True:
    resposta = menu([mlist[0], mlist[1], mlist[2], mlist[3], mlist[4], mlist[5], mlist[6], mlist[7], mlist[8], mlist[9]])
    if resposta == 1:
        print('{}'.format(op1))
        os.system('cls') or None
        exec(open("./funcoes/conexao_seanet.py").read())
    elif resposta == 2:
        print('{}'.format(op2))
        os.system('cls') or None
        abrir_taref()
    elif resposta == 3:
        os.system('cls') or None
        print('{}'.format(op3), 'Testes de rede', '\n')
        abrir_avanc()
    elif resposta == 4:
        os.system('cls') or None
        print('{}'.format(op4), 'Validacao Automatizada', '\n')
        abrir_autom()
    elif resposta == 5:
        os.system('cls') or None
        print('{}'.format(op5), 'Monitoracao da conexao', '\n')
        abrir_aplic()
    elif resposta == 6:
        print('{}'.format(op6))
        os.system('cls') or None
        abrir_wsl()
    elif resposta == 7:
        os.system('cp -r C:/sistema_python/comp_git/git_pull.py C:/scripts_logs')
        os.chdir(myfile_cp_logs)
        os.startfile('git_pull.py')
    elif resposta == 8:
        os.system('cls') or None
        print('{}'.format(op8, 'Site em HTML'))
        os.startfile('aplication.html')
    elif resposta == 9:
        gerar_print()
    elif resposta == 10:
        funcao_sair()
    else:
        leia_opcao()
        sleep(2)

