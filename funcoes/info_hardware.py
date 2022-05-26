
#------------------------------------------------

import os
from variaveis.interface_config import *
import subprocess
from termcolor import colored

#------------------------------------------------

def cabecalho_info(txt):
    print('-' * 42)
    print(colored(txt.center(42), 'red', attrs=['bold']))
    print('-' * 42)


#------------------------------------------------
# infos de hardware

def info_hardware():
    os.system('cls') or None
    cabecalho_info('Informacoes da Placa Mae')
    os.system('wmic baseboard get product,Manufacturer,version,serialnumber')
    cabecalho_info('Informacoes de Rede')
    print('\nInterfaces de REDE - Detalhes')
    os.system(' /scripts/funcoes/interface_rede.ps1')
    print('\nDados foram carregados em nova aba.')
    dados_pc()
    os.system('start C:\Windows\System32\cmd.exe /k %windir%\system32\ipconfig.exe')
    os.system('start C:\Windows\System32\msinfo32.exe')


#------------------------------------------------
# funcoes de teste na rede

def traceroute():
    func_cabecalho('Excutando um Traceroute na Seanet')
    subprocess.run(["tracert", ping_seanet])
    func_cabecalho('Excutando um Pathping na Seanet')
    subprocess.run(["pathping", ping_seanet])
    dados_pc()

#------------------------------------------------
# Rotas de rede

def route():
    func_cabecalho('Executando um Route Print')
    subprocess.run(["route", "print"])
    dados_pc()

#------------------------------------------------
# Antigo infos_windows


def versao_windows():
    func_cabecalho('Detalhes da versao do SO')
    print('\n')
    subprocess.run(["wmic", "os", "get", "buildnumber,caption,CSDVersion"])
    subprocess.run(["wmic", "OS", "get", "OSArchitecture"])
    dados_pc()
    subprocess.run(["winver"])

def system_info():
    func_cabecalho('Informacoes do Windows')
    subprocess.run(["systeminfo"])
    dados_pc()