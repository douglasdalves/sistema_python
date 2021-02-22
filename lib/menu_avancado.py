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
    resposta = menu(['TraceRouter e Pathping','Testar o DNS','Testar com Netstat','Teste1','Captura de Tela','Retornar ao Home'])
    if resposta == 1:
        os.system('cls') or None
        print('Opção 1 - Testes do Trace na Seanet')
        exec(open("./funcoes/trace_na_seanet.py").read())
        #print('\n')
    elif resposta == 2:
        os.system('cls') or None
        os.system('start ./funcoes/consulta_dns.py')
    elif resposta == 3:
        print('Opção 3 - Testando a Rede em Netstat')
        os.system('cls') or None
        os.system('start ./funcoes/netstat_rede.py')
    elif resposta == 4:
        print('Opção 4 - Test')
    elif resposta == 5:
        print('Opção 5 - Captura de Tela')
        capturar = pyautogui.screenshot()
        capturar.save('print.png')
    elif resposta == 6:
        os.system('cls') or None
        retorno('Retornando para o menu principal')
        exec(open("sistema.py").read())
    else:
        leia_opcao()
        sleep(2)