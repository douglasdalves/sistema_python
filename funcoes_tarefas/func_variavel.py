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

myfile_bkp = r'C:/scripts_logs/info_path/backupPATH.txt'
myfile_path = r'C:/scripts_logs/info_path/PATH*'
myfile_sh = r'C:/scripts/automacao_sh/altera_path.sh'

#------------------------------------------------
# funcoes de variaveis

cabecalho('Variavel de Ambiente W10')

print(colored('Consultar o conteudo da PATH.', 'blue', attrs=['bold']))
print('\n')
gera_path = os.system('echo %PATH%')
print('\n')

print(colored('Backup da PATH realizado', 'blue', attrs=['bold']))
os.system('echo %PATH% > C:/scripts_logs/info_path/backupPATH.txt')
subprocess.call(["ls", "-l", myfile_bkp])

cabecalho('Arquivo alterado')
subprocess.call(myfile_sh, shell=True)
subprocess.call(["ls", "-l", myfile_path])
print('\n')
print('Backup efetuado para a pasta Scripts_logs')
print('\n')


