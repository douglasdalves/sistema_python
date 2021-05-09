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
os.system('hostname > ./bkp_arquivos/backupPATH.txt')
os.system('echo %PATH% >> ./bkp_arquivos/backupPATH.txt')
os.system('ls -ltr ./bkp_arquivos/backupPATH.txt')
print('\n')
print('Backup efetuado para o arquivo.TXT')
print('\n')