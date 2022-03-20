#------------------------------------------------
#Importacao de dados

from variaveis.interface_config import *
from funcoes_tarefas.func_wsl import *
from time import sleep
import os


#------------------------------------------------
#Linhas de personalizacao

finalizar_docker="W:\home\douglas\scripts\stop_docker.sh"

# Dados menu
t_menu = 'Status da WSL'
t_menu1 = 'Iniciando a WSL'
t_menu2 = 'Start do Docker'
t_menu3 = 'Stop do Docker'
t_menu4 = 'Retornar ao Home'

#------------------------------------------------
#Codigo do menu 6

def abrir_wsl():
    while True:
        resposta = menu_secund([t_menu,t_menu1,t_menu2,t_menu3,t_menu4])
        if resposta == 1:
            os.system('cls') or None
            wsl_status()
        elif resposta == 2:
            print('{}'.format(op2))
            os.system('cls') or None
            os.system('Start Ubuntu')
        elif resposta == 3:
            print('{}'.format(op3))
        elif resposta == 4:
            print('{}'.format(op4))
            finalizar_docker
        elif resposta == 5:
            print('{}'.format(op5))
            frase_retorno()
        elif resposta == 6:
            print('{}'.format(op6))
        elif resposta == 7:
            print('{}'.format(op7), 'Captura de Tela')
            gerar_print()
        elif resposta == 8:
            frase_retorno()
        else:
            leia_opcao()
            sleep(2)