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
os.system('pip list > ./bkp_arquivos/backupPIP_python.txt')
os.system('ls -ltr ./bkp_arquivos/backupPIP_python.txt')
print('\n')
print('Backup efetuado para o arquivo.TXT')


#subprocess.run(["ls", "-ltr",])
#os.system('ls -ltr PIP_python*')

func_cabecalho('Pacotes do Python')

#------------------------------------------------
# chamar a instalacao de pacotes

while True:
    print('Funcoes: 1-Instalar / 2-Nao instalar')
    print('         3-Altera arquivos de BKP')
    print('\n')
    aplicar = str(input('Voce quer aplicar pacotes do Python? '))
    if aplicar == '1':
        print('\n')
        exec(open("pacotes_config.bat").read())
        print('\n')
    elif aplicar == '2':
        func_cabecalho('Tudo bem volte quando quiser')
        break
    else:
        aplicar == '3'
        os.system('start ./automacao_sh/altera_pacote.sh')
        print('\n')
        print('Backup efetuado para o arquivo.TXT')
        print('\n')
        #os.chdir('.\scripts\bkp_arquivos')
        #subprocess.popen(["/scripts/bkp_arquivos", "ls", "-ltr"])

dados_pc()

#os.system('start C:\Windows\System32\cmd.exe /k %windir%\system32\ipconfig.exe')
#os.system(' /scripts/funcoes/interface_rede.ps1')