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
    r = dict()
    #subprocess.run(["ping", "-n", "4", ping_alexa])
    r[subprocess.run(["ping", "-n", "4", ping_plug1])] = func_cabecalho('Smart plug 1')
    r[subprocess.run(["ping", "-n", "4", ping_plug2])] = func_cabecalho('Smart plug 2')
    r[subprocess.run(["ping", "-n", "4", ping_controle])] = func_cabecalho('Smart Controle wi-fi')
    r[subprocess.run(["ping", "-n", "4", ping_lampada])] = func_cabecalho('Smart Lampada')
    r[subprocess.run(["ping", "-n", "4", ping_lampada2])] = func_cabecalho('Smart Lampada 2')
    r[subprocess.run(["ping", "-n", "4", ping_plafon])] = func_cabecalho('Smart Plafon')
    r[subprocess.run(["ping", "-n", "4", ping_fita_led])] = func_cabecalho("Smart Fita RGB")
    r[subprocess.run(["ping", "-n", "4", ping_sonoff1])] = func_cabecalho("Interupator Sonoff")
    r[subprocess.run(["ping", "-n", "4", ping_sonoff2])] = func_cabecalho("Interupator Sonoff 2")
    r[subprocess.run(["ping", "-n", "4", ping_interruptor_sala])] = func_cabecalho("Interupator Sala")
    r[subprocess.run(["ping", "-n", "4", ping_interruptor_cozinha])] = func_cabecalho("Interupator Cozinha")
    r[subprocess.run(["ping", "-n", "4", ping_interruptor_banheiro])] = func_cabecalho("Interupator Banheiro")
    r[subprocess.run(["ping", "-n", "4", ping_interruptor_suite])] = func_cabecalho("Interupator Quarto")
    dados_pc()


def ping_not():
    os.system('cls') or None
    r = dict()
    r[subprocess.run(["ping", "-n", "4", ping_tab_s7])] = func_cabecalho('Galaxy Tab S7')
    r[subprocess.run(["ping", "-n", "4", ping_kindle])] = func_cabecalho('Amazom Kindle')
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
    r[subprocess.run(["ping", "-n", "4", ping_dell])] = func_cabecalho('Notebook Working')
    dados_pc()


def ping_equipamentos():
    os.system('cls') or None
    func_cabecalho('Roteador - C5')
    requesicao_tplink = requests.get("http://192.168.8.1/")
    print(f'\nHTTP Status do Roteador: {requesicao_tplink}','\n')
    subprocess.run(["ping", "-n", "4", ping_roteador])
    r = dict()
    func_cabecalho('Echo Dot - Alexa')
    requisicao_echo3 = requests.get("https://alexa.amazon.com.br/spa/index.html?#settings/device/G0911W110342050A")
    requisicao_echo4 = requests.get("https://alexa.amazon.com.br/spa/index.html?#settings/device/G091AA1220270BJ6")
    print('\nHTTP Status Code da Alexa', '\n', f'Status code Echo Escritorio: {requisicao_echo3}', '\n', f'Status code Echo Sala: {requisicao_echo4}')
    r[subprocess.run(["ping", "-n", "4", ping_tv])] = func_cabecalho('Smart TV - LG')
    r[subprocess.run(["ping", "-n", "4", ping_robo_aspirador])] = func_cabecalho("Robo Aspirador")
    r[subprocess.run(["ping", "-n", "4", ping_lavaeseca])] = func_cabecalho("Samsung Lava e Seca")
    r[subprocess.run(["ping", "-n", "4", ping_fechadura])] = func_cabecalho("Smart Fechadura")
    r[subprocess.run(["ping", "-n", "4", ping_ar18])] = func_cabecalho("Ar Condicionado sala")
    r[subprocess.run(["ping", "-n", "4", ping_ar9])] = func_cabecalho("Ar Condicionado Quarto")
    dados_pc()