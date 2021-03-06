
#------------------------------------------------

import os
from funcoes.interface_test import *
import subprocess
from termcolor import colored

#------------------------------------------------

def linha_info(tam = 42):
    return '-' * tam

def cabecalho_info(txt):
    print(linha_info())
    print(txt.center(42))
    print(linha_info())

#------------------------------------------------
# infos de hardware

def info_hardware():
    os.system('cls') or None
    cabecalho_info('Informacoes da Placa Mae')
    os.system('wmic baseboard get product,Manufacturer,version,serialnumber')
    cabecalho_info('Informacoes de Rede')
    print('\n')
    print('Interfaces de REDE - Detalhes')
    os.system(' /scripts/funcoes/interface_rede.ps1')
    print('\n')
    print('Dados foram carregados em nova aba.')
    dados_pc()
    os.system('start C:\Windows\System32\cmd.exe /k %windir%\system32\ipconfig.exe')
    os.system('start C:\Windows\System32\msinfo32.exe')


#------------------------------------------------
# funcoes de teste na rede

def traceroute():
    func_cabecalho('Excutando um Traceroute na Seanet')
    subprocess.run(["tracert", "186.251.248.1"])
    func_cabecalho('Excutando um Pathping na Seanet')
    subprocess.run(["pathping", "186.251.248.1"])
    dados_pc()