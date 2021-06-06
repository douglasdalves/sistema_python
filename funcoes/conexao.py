#--------------------------------------------
# configuracoes

import sys
import os
import subprocess
from termcolor import colored
from funcoes.interface_test import *


#------------------------------------------------
# testes via curl

def test_conexao():
    print('\n')
    print('HTTP Status Code da Pagina speedtest.net')
    os.system('curl --write-out %{http_code} --silent --output /dev/null https://www.speedtest.net/pt')


def alexa_conexao():
    print('\n')
    print('HTTP Status Code da Alexa:')
    os.system('curl --write-out %{http_code} --silent --output /dev/null https://alexa.amazon.com.br/spa/index.html')
    print('\n')


def roteador_conexao():
    print('\n')
    print('HTTP Status do Roteador:')
    os.system('curl --write-out %{http_code} --silent --output /dev/null http://192.168.8.1/')
    print('\n')

#------------------------------------------------
# funcoes do ping

def ping_smarthome():
    os.system('cls') or None
    func_cabecalho('Roteador - C60')
    roteador_conexao()
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



def ping_not():
    os.system('cls') or None
    func_cabecalho('Notebook Douglas')
    subprocess.run(["ping", "-n", "4", "192.168.8.101"])
    func_cabecalho('Notebook Marcia')
    subprocess.run(["ping", "-n", "4", "192.168.8.102"])
    dados_pc()

def ping_telefones():
    os.system('cls') or None
    func_cabecalho('Smartphone Redmi k20')
    subprocess.run(["ping", "-n", "4", "192.168.8.104"])
    func_cabecalho('Smartphone Mi 8 lite')
    subprocess.run(["ping", "-n", "4", "192.168.8.105"])
    dados_pc()
