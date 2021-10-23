#--------------------------------------------
# configuracoes

import os
import subprocess
import requests
from termcolor import colored
from variaveis.interface_config import *


#------------------------------------------------
# testes via curl


def test_conexao():
    print('\n')
    print('HTTP Status Code da Pagina speedtest.net')
    os.system('curl --write-out %{http_code} --silent --output /dev/null https://www.speedtest.net/pt')


def alexa_conexao():
    print('\n')
    print('HTTP Status Code da Alexa:')
    requisicao_alexa = requests.get("https://alexa.amazon.com.br/spa/index.html")
    print(requisicao_alexa)
    #os.system('curl --write-out %{http_code} --silent --output /dev/null https://alexa.amazon.com.br/spa/index.html')
    print('\n')


def roteador_conexao():
    print('\n')
    print('HTTP Status do Roteador:')
    requesicao_tplink = requests.get("http://192.168.8.1/")
    print(requesicao_tplink)
    #os.system('curl --write-out %{http_code} --silent --output /dev/null http://192.168.8.1/')
    print('\n')

#------------------------------------------------
# funcoes do ping


def ping_seanet():
    func_cabecalho('Ping 40x para o IP da Seanet')
    subprocess.run(["ping", "-n", "40", ping_seanet])
    #os.system('ping -n 40 186.251.248.1')
    #os.system('ping -n 8 192.168.246.17') #ip da vpn
    dados_pc()


def ping_smarthome():
    os.system('cls') or None
    func_cabecalho('Roteador - C60')
    roteador_conexao()
    subprocess.run(["ping", "-n", "4", ping_roteador])
    func_cabecalho('Smart TV - LG')
    subprocess.run(["ping", "-n", "4", ping_tv])
    func_cabecalho('Echo Dot - Alexa')
    alexa_conexao()
    subprocess.run(["ping", "-n", "4", ping_alexa])
    func_cabecalho('Smart plug 1')
    subprocess.run(["ping", "-n", "4", ping_plug1])
    func_cabecalho('Smart plug 2')
    subprocess.run(["ping", "-n", "4", ping_plug2])
    func_cabecalho('Smart Lampada')
    subprocess.run(["ping", "-n", "4", ping_lampada])
    dados_pc()



def ping_not():
    os.system('cls') or None
    func_cabecalho('Notebook Douglas')
    subprocess.run(["ping", "-n", "4", ping_acer])
    func_cabecalho('Notebook Marcia')
    subprocess.run(["ping", "-n", "4", ping_not_mor])
    dados_pc()

def ping_telefones():
    os.system('cls') or None
    func_cabecalho('Smartphone Redmi k20')
    subprocess.run(["ping", "-n", "4", ping_mi9])
    func_cabecalho('Smartphone Mi 8 lite')
    subprocess.run(["ping", "-n", "4", ping_mi8])
    dados_pc()

def ping_desktop():
    os.system('cls') or None
    func_cabecalho('Teste Desktop WI-FI')
    subprocess.run(["ping", "-n", "4", ping_pc])
    dados_pc()
