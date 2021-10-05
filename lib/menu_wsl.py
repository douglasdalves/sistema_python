#------------------------------------------------
#Importacao de dados

from variaveis.interface_config import *
from funcoes_tarefas.func_wsl import *
from time import sleep
import os


#------------------------------------------------
#Linhas de personalizacao

finalizar_docker="W:\home\douglas\scripts\stop_docker.sh"

#------------------------------------------------
#Codigo do menu 5

def abrir_wsl():
    while True:
        resposta = menu_secund(['Status da WSL','Iniciando a WSL','Start do Docker','Stop do Docker','Retornar ao Home'])
        if resposta == 1:
            os.system('cls') or None
            wsl_status()
        elif resposta == 2:
            print('Opcao 2 -')
            os.system('cls') or None
            os.system('Start Ubuntu')
        elif resposta == 3:
            print('Opcao 3 -')
        elif resposta == 4:
            print('Opcao 4 -')
            finalizar_docker
        elif resposta == 5:
            print('Opcao 5 -')
            frase_retorno()
        elif resposta == 6:
            print('Opcao 6 -')
        elif resposta == 7:
            print('Opcao 7 - Captura de Tela')
            gerar_print()
        elif resposta == 8:
            frase_retorno()
        else:
            leia_opcao()
            sleep(2)