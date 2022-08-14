#--------------------------------------------
# configuracoes


import requests
from termcolor import colored
from variaveis.interface_config import *

#------------------------------------------------
# testes via curl

def test_conexao():
    #os.system('curl --write-out %{http_code} --silent --output /dev/null https://www.speedtest.net/pt')
    requisicao_speedtest = requests.get("https://www.speedtest.net/pt")
    print(f'\nHTTP Status Code da Pagina speedtest.net: {requisicao_speedtest}')


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
    requesicao_tplink = requests.get("http://192.168.8.1/")
    print(f'\nHTTP Status do Roteador: {requesicao_tplink}','\n')
    subprocess.run(["ping", "-n", "4", ping_roteador])
    r = dict()
    r[subprocess.run(["ping", "-n", "4", ping_tv])] = func_cabecalho('Smart TV - LG')
    func_cabecalho('Echo Dot - Alexa')
    requisicao_echo3 = requests.get("https://alexa.amazon.com.br/spa/index.html?#settings/device/G0911W110342050A")
    requisicao_echo4 = requests.get("https://alexa.amazon.com.br/spa/index.html?#settings/device/G091AA1220270BJ6")
    print('\nHTTP Status Code da Alexa', '\n', f'Status code Echo Escritorio: {requisicao_echo3}', '\n', f'Status code Echo Sala: {requisicao_echo4}')
    #subprocess.run(["ping", "-n", "4", ping_alexa])
    r[subprocess.run(["ping", "-n", "4", ping_plug1])] = func_cabecalho('Smart plug 1')
    r[subprocess.run(["ping", "-n", "4", ping_plug2])] = func_cabecalho('Smart plug 2')
    r[subprocess.run(["ping", "-n", "4", ping_controle])] = func_cabecalho('Smart Controle wi-fi')
    r[subprocess.run(["ping", "-n", "4", ping_lampada])] = func_cabecalho('Smart Lampada')
    r[subprocess.run(["ping", "-n", "4", ping_lampada2])] = func_cabecalho('Smart Lampada 2')
    r[subprocess.run(["ping", "-n", "4", ping_sonoff1])] = func_cabecalho("Interupator Sonoff")
    r[subprocess.run(["ping", "-n", "4", ping_sonoff2])] = func_cabecalho("Interupator Sonoff 2")
    dados_pc()


def ping_not():
    os.system('cls') or None
    r = dict()
    r[subprocess.run(["ping", "-n", "4", ping_acer])] = func_cabecalho('Notebook Douglas')
    r[subprocess.run(["ping", "-n", "4", ping_not_mor])] = func_cabecalho('Notebook Marcia')
    r[subprocess.run(["ping", "-n", "4", ping_dell])] = func_cabecalho('Notebook Compass.uol')
    dados_pc()


def ping_telefones():
    os.system('cls') or None
    r = dict()
    r[subprocess.run(["ping", "-n", "4", ping_mi9])] = func_cabecalho('Smartphone Redmi k20')
    r[subprocess.run(["ping", "-n", "4", ping_mi8])] = func_cabecalho('Smartphone Mi 8 lite')
    dados_pc()


def ping_desktop():
    os.system('cls') or None
    r = dict()
    r[subprocess.run(["ping", "-n", "4", ping_pc])] = func_cabecalho('Desktop Escritorio')
    dados_pc()
