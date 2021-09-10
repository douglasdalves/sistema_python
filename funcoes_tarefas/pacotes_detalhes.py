import os
import sys
import subprocess
from termcolor import colored
from variaveis.interface_config import *


#--------------------------------------------
# configuracoes do menu


func_cabecalho('Lista os Pacotes do Python')
print('\n')
subprocess.run(["pip", "list",])
os.system('pip list > ./bkp_arquivos/backupPIP_python.txt')
subprocess.run(["ls", "-ltr", myfile_bkp_pip])
print('\n')
print('Backup efetuado para o arquivo.TXT')

#subprocess.run(["ls", "-ltr",])


func_cabecalho('Pacotes do Python')

#------------------------------------------------
# chamar a instalacao de pacotes

aplicar = 0
while aplicar != 3:
    print('''Funcoes: 
    [1] Instalar
    [2] Nao instalar
    [3] Altera arquivos de BKP''')
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