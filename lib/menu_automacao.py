#------------------------------------------------
#Importacao de dados

from lib.aplicacao_interface import *
from time import sleep
import os
import pyautogui
import subprocess


#------------------------------------------------
#Linhas de personalizacao



#------------------------------------------------
#Codigo do menu 5

while True:
    resposta = menu(['Versao do Windows','Detalhes do Windows','Informacao do Hardware','Relatorio de bateria','Testes1','Testes2','Captura de Tela','Retornar ao Home'])
    if resposta == 1:
        os.system('cls') or None
        print('Opcao 1 - Detalhes da Build do SO')
        exec(open("./funcoes/versao_windows.py").read())
    elif resposta == 2:
        print('Opcao 2 - Detalhes do HardWare')
        os.system('cls') or None
        exec(open("./funcoes/system_info.py").read())
    elif resposta == 3:
        print('Opcao 3 - Info de Hardware')
        os.system('cls') or None
        exec(open("./funcoes/info_hardware.py").read())
    elif resposta == 4:
        print('Opcao 4 - Bateria')
        os.system('cls') or None
        exec(open("./funcoes/conexao2.py").read())
    elif resposta == 5:
        print('Opcao 5 - test1')
    elif resposta == 6:
        print('Opcao 6 - test2')
    elif resposta == 7:
        print('Opcao 7 - Captura de Tela')
        gerar_print_aplicacao()
    elif resposta == 8:
        frase_retorno()
    else:
        leia_opcao()
        sleep(2)