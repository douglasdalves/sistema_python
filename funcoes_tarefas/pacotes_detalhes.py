import os
import sys
import subprocess
from termcolor import colored
from funcoes.interface_test import *

#--------------------------------------------
# configuracoes do menu

func_cabecalho('Lista os Pacotes do Python')
print('\n')
os.system('pip list')

func_cabecalho('Pacotes do Python')

#------------------------------------------------
# chamar a instalacao de pacotes

while True:
    print('Funcoes: 1-Instalar / 2-Nao instalar')
    print('\n')
    aplicar = str(input('Voce quer aplicar pacotes do Python? '))
    if aplicar == '1':
        print('\n')
        exec(open("pacotes_config.bat").read())
        print('\n')
    else:
        aplicar == '2'
        func_cabecalho('Tudo bem volte quando quiser')
        break

dados_pc()

#os.system('start C:\Windows\System32\cmd.exe /k %windir%\system32\ipconfig.exe')
#os.system(' /scripts/funcoes/interface_rede.ps1')