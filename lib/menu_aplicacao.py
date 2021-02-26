#------------------------------------------------
#Importacao de dados

from lib.aplicacao_interface import *
from time import sleep
import os
import pyautogui
import subprocess
import webbrowser

#------------------------------------------------
# funcao test de status do http

def test_conexao():
    print('\n')
    print('HTTP Status Code da Pagina speedtest.net')
    os.system('curl --write-out %{http_code} --silent --output /dev/null www.google.com.br')

#test_conexao()


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
        os.system('start ./funcoes/ping_seanet.py')
        #exec(open("./funcoes/ping_seanet.py").read())
    elif resposta == 3:
        print('Opção 3 - Testar conectividade dos Smart homes')
        os.system('cls') or None
        exec(open("./funcoes/conexao1.py").read())
    elif resposta == 4:
        print('Opção 4 - Testar a conectividade dos Notebooks')
        os.system('cls') or None
        exec(open("./funcoes/conexao2.py").read())
    elif resposta == 5:
        print('Opção 5 - Testar a conectividade dos Smartphones')
        os.system('cls') or None
        exec(open("./funcoes/conexao3.py").read())
    elif resposta == 6:
        print('Opção 6 - test')
    elif resposta == 7:
        print('Opção 7 - Captura de Tela')
        capturar = pyautogui.screenshot()
        capturar.save('print.png')
    elif resposta == 8:
        os.system('cls') or None
        retorno('Retornando para o menu principal')
        exec(open("sistema.py").read())
    else:
        leia_opcao()
        sleep(2)