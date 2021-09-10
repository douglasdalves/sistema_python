import os
from termcolor import colored
import sys
import subprocess
#from funcoes.interface_test import *

def linha(tam = 42):
    return '-' * tam

def cabecalho (txt):
    print('\n')
    print(linha())
    print(txt.center(42))
    print(linha())
    print('\n')

#------------------------------------------------
# funcoes de variaveis

cabecalho('Variavel de Ambiente W10')

print(colored('Consultar o conteudo da PATH.', 'blue', attrs=['bold']))
print('\n')
os.system('echo %PATH%')
print('\n')

print(colored('Realizar o BKP da PATH', 'blue', attrs=['bold']))
os.system('echo %PATH% > ./bkp_arquivos/backupPATH.txt')
os.system('ls -ltr ./bkp_arquivos/backupPATH.txt')
print('\n')
print('Backup efetuado para o arquivo.TXT')
print('\n')



#------------------------------------------------
# chamar a instalacao de pacotes

aplicar = 0
while aplicar != 3:
    print('''Funcoes:
    [1] Voltar ao menu
    [2] Realizar arquivo de BKP''')
    print('\n')
    aplicar = str(input('Digite uma das opcoes? '))
    if aplicar == '1':
        cabecalho('Tudo bem volte quando quiser')
        break
    else:
        aplicar == '2'
        os.system('start ./automacao_sh/altera_path.sh')
        print('\n')
        print('Backup efetuado para o arquivo.TXT')
        print('\n')
