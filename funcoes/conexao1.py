import os
import subprocess
from termcolor import colored
from funcoes.interface_test import *

#------------------------------------------------
# configuracao de linhas

def linha(tam = 42):
    return '-' * tam

def cabecalho (txt):
    print('\n')
    print(linha())
    print(txt.center(42))
    print(linha())

#------------------------------------------------
# testes via curl

def alexa_conexao():
    print('\n')
    print('HTTP Status Code da Alexa:')
    os.system('curl --write-out %{http_code} --silent --output /dev/null https://alexa.amazon.com.br/spa/index.html')
    print('\n')

#alexa_conexao()

def roteador_conexao():
    print('\n')
    print('HTTP Status do Roteador:')
    os.system('curl --write-out %{http_code} --silent --output /dev/null http://192.168.8.1/')
    print('\n')

#------------------------------------------------
# funcoes do ping


func_cabecalho('Roteador - C60')
roteador_conexao()
#os.system('ping -n 3 192.168.8.1')
subprocess.run(["ping", "-n", "4", "192.168.8.1"])


func_cabecalho('Smart TV - LG')
subprocess.run(["ping", "-n", "4", "192.168.8.103"])


func_cabecalho('Echo Dot - Alexa')
alexa_conexao()
subprocess.run(["ping", "-n", "4", "192.168.8.107"])


func_cabecalho('Smart plug 1')
subprocess.run(["ping", "-n", "4", "192.168.8.108"])


func_cabecalho('Smart plug 2')
subprocess.run(["ping", "-n", "4", "192.168.8.109"])

func_cabecalho('Smart Lampada')
subprocess.run(["ping", "-n", "4", "192.168.8.110"])
dados_pc()