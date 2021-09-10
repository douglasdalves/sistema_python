#------------------------------------------------
#Importacao de dados

from variaveis.interface_config import *
from funcoes_tarefas.func_wsl import *
from time import sleep
import os


#------------------------------------------------
#Linhas de personalizacao



#------------------------------------------------
#Codigo do menu 5

while True:
    resposta = menu_secund(['Status da WSL','Iniciando a WSL','Start do Docker','Retornar ao Home'])
    if resposta == 1:
        os.system('cls') or None
        wsl_status()
    elif resposta == 2:
        print('Opcao 2 - Detalhes do HardWare')
        os.system('cls') or None
    elif resposta == 3:
        print('Opcao 3 - Info de Hardware')
    elif resposta == 4:
        print('Opcao 4')
        frase_retorno()
    elif resposta == 5:
        print('Opcao 5 - Rotas do Windows')
    elif resposta == 6:
        print('Opcao 6 - test2')
    elif resposta == 7:
        print('Opcao 7 - Captura de Tela')
        gerar_print()
    elif resposta == 8:
        frase_retorno()
    else:
        leia_opcao()
        sleep(2)