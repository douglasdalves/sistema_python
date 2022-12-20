import os
from termcolor import colored
import subprocess
from variaveis.interface_config import *

#------------------------------------------------

def linha_git(tam = 42):
    return '-' * tam

def cabecalho_git (txt):
    print('\n')
    print(linha_git())
    print(txt.center(42))
    print(linha_git())
    print('\n')

#------------------------------------------------
# funcoes do cenario git

def notas_git():
    cabecalho_git('Funcoes do GitHub')

    os.chdir('C:\scripts') #Altere o diretório de trabalho atual
    print ("Voce esta em: %s" % os.getcwd()) #Retorna o diretório de trabalho atual

    print(colored('Lista o Repositorio remoto:', 'blue', attrs=['bold']))
    os.system('git remote -v')
    print(colored('Lista as branchs:', 'blue', attrs=['bold']))
    os.system('git branch')
    print('\n')
    os.system('git status')
    print('\n')
    os.system('git log -n 2')

    dados_pc()

#https://pt.stackoverflow.com/questions/6188/como-copiar-commits-de-um-branch-para-o-outro