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
os.system('pip list > C:/scripts_logs/info_pacotes/backupPIP_python.txt')
subprocess.run(["ls", "-ltr", myfile_bkp_pip])
print('\n')
print('Backup efetuado para o arquivo.TXT')




func_cabecalho('Pacotes do Python')

#------------------------------------------------
# chamar a instalacao de pacotes

myfile_pacote = r'C:/scripts/automacao_sh/altera_pacote.sh'

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
        os.startfile(myfile_pacote)
        print('\n')
        print('Backup efetuado para o arquivo.TXT')
        print('\n')

dados_pc()

        #os.chdir('.\scripts\bkp_arquivos')
        #subprocess.popen(["/scripts/bkp_arquivos", "ls", "-ltr"])

#os.system('start C:\Windows\System32\cmd.exe /k %windir%\system32\ipconfig.exe')
#os.system(' /scripts/funcoes/interface_rede.ps1')