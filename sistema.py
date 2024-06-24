#------------------------------------------------
#Importacao de dados

from email.mime import application
from lib.menu_tarefas import abrir_taref
from lib.menu_avancado import abrir_avanc
from lib.menu_automacao import abrir_autom
from lib.menu_wsl import abrir_wsl

from variaveis.interface_config import *
from time import sleep

from termcolor import colored
from funcoes import *
from lib import *


#------------------------------------------------

myfile_cp_logs = r'C:/scripts_logs'

# Dados menu em lista
mlist = ['Teste de Conexao ao Provedor', 'Agilizando Tarefas', 'Test de Rede', 'Testes Automatizados', 'Tarefas em WSL','Web system', 'Captura de Tela', 'Sair']

#------------------------------------------------
#Codigo do menu principal


while True:
    resposta = menu([mlist[0], mlist[1], mlist[2], mlist[3], mlist[4], mlist[5], mlist[6], mlist[7]])
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
        print('{}'.format(op5))
        os.system('cls') or None
        abrir_wsl()
    elif resposta == 6:
        os.system('cls') or None
        print('{}'.format(op7, 'Site em HTML'))
        os.startfile('aplication.html')
    elif resposta == 7:
        gerar_print()
    elif resposta == 8:
        funcao_sair()
    else:
        leia_opcao()
        sleep(2)