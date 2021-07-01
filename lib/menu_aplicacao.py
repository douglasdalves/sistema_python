#------------------------------------------------
#Importacao de dados

from platform import python_branch
from lib.aplicacao_interface import *
from funcoes.conexao import *
from time import sleep
import os
import pyautogui
import subprocess
import webbrowser
import sys

##########
# exemplos

    #os.path(myfile.conexao_seanet.py)
    #subprocess.Popen(ping_telefones(), shell=True)
    #webbrowser.open_new_tab('www.speedtest.net')
    #exec(open("./funcoes/ping_seanet.py").read())

##########

#------------------------------------------------
# 

myfile="C:/scripts/funcoes/conexao_seanet.py"



#------------------------------------------------
#Codigo do menu 5

while True:
    resposta = menu(['Abrir o Chrome para testes','Ping da Conexao','Conectividade - Smart home','Conectividade - Notebooks','Conectividade - Smartphones','Conectividade - Desktop','Captura de Tela','Retornar ao Home'])
    if resposta == 1:
        os.system('cls') or None
        print('Opcao 1 - Abrindo o navegor padrao')
        test_conexao()
        os.system('start ./funcoes/browserbot.py')
        print('\n')
    elif resposta == 2:
        os.system('cls') or None
        #os.system('start ./funcoes/conexao_seanet.py')
    elif resposta == 3:
        print('Opcao 3 - Testar conectividade dos Smart homes')
        ping_smarthome()
    elif resposta == 4:
        print('Opcao 4 - Testar a conectividade dos Notebooks')
        ping_not()
    elif resposta == 5:
        print('Opcao 5 - Testar a conectividade dos Smartphones')
        ping_telefones()
    elif resposta == 6:
        print('Opcao 6 - Testar a conectividade do Desktop')
        ping_desktop()
    elif resposta == 7:
        print('Opcao 7 - Captura de Tela')
        gerar_print_aplicacao()
    elif resposta == 8:
        frase_retorno()
    else:
        leia_opcao()
        sleep(2)