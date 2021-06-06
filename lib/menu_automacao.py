#------------------------------------------------
#Importacao de dados

from lib.aplicacao_interface import *
from funcoes.infos_windows import *
from funcoes.info_hardware import *
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
        versao_windows()
    elif resposta == 2:
        print('Opcao 2 - Detalhes do HardWare')
        os.system('cls') or None
        system_info()
    elif resposta == 3:
        print('Opcao 3 - Info de Hardware')
        info_hardware()
    elif resposta == 4:
        print('Opcao 4')
        os.system('cls') or None
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