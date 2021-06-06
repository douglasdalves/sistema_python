#------------------------------------------------
#Importacao de dados

from lib.aplicacao_interface import *
from funcoes.conexao import *
from time import sleep
import os
import pyautogui
import subprocess
import webbrowser
import sys

#------------------------------------------------
# funcao test de status do http



#------------------------------------------------
#Codigo do menu 5

while True:
    resposta = menu(['Abrir o Chrome para testes','Ping da Conexao','Conectividade - Smart home','Conectividade - Notebooks','Conectividade - Smartphones','Testes2','Captura de Tela','Retornar ao Home'])
    if resposta == 1:
        os.system('cls') or None
        print('Opcao 1 - Abrindo o navegor padrao')
        #exec(open("./funcoes/browserbot.py").read())
        test_conexao()
        os.system('start ./funcoes/browserbot.py')
        #webbrowser.open_new_tab('www.speedtest.net')
        print('\n')
    elif resposta == 2:
        os.system('cls') or None
        os.system('start ./funcoes/conexao_seanet.py')
        #exec(open("./funcoes/ping_seanet.py").read())
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
        print('Opcao 6 - test')
    elif resposta == 7:
        print('Opcao 7 - Captura de Tela')
        gerar_print_aplicacao()
    elif resposta == 8:
        frase_retorno()
    else:
        leia_opcao()
        sleep(2)