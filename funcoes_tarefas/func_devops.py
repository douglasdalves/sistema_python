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
# funcoes do cenario git

cabecalho('Funcoes em Vagrant')

print(colored('Permite ver todas as maquinas que estao rodando.', 'blue', attrs=['bold']))
print('\n')
os.system('vagrant global-status')
print('\n')

print(colored('Permite ver quais os boxes que estao instalados.', 'blue', attrs=['bold']))
print('\n')
os.system('vagrant box list')

cabecalho('Funcoes em Docker')
print('Obs: Usando Toolbox')

print(colored('Permite ver detalhes da VM.', 'blue', attrs=['bold']))
print('\n')
os.system('docker-machine ls')
print('\n')