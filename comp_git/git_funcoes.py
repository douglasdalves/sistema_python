import os
from termcolor import colored
import sys
import subprocess
from variaveis.interface_config import *

#------------------------------------------------
# variaveis

git_oneline = "os.system('git log --oneline') #exibicao de log do git"

#------------------------------------------------
# configuracoes de css

def linha_git(tam = 42):
    return '-' * tam

def cabecalho_git (txt):
    print('\n')
    print(linha_git())
    print(txt.center(42))
    print(linha_git())
    print('\n')

#------------------------------------------------
# Aplicar alteracoes

def func_commit():
    print('\n')
    os.system('git branch')
    print('\nCerto vou aplicar o git add .')
    os.system('git add .')
    print('\n')
    print(colored('Agora precisa commitar, digite abaixo..', 'red'))
    print('ex: git commit -m "msg"', '\n')
    os.system(input())
    print('\n')
    git_oneline


def func_github():
    print('\n', 'Enviando dados ao Git Hub')
    #os.chdir('C:\sistema_git') #Altere o diretório de trabalho atual
    #print ("Voce esta em: %s" % os.getcwd()) #Retorna o diretório de trabalho atual
    print('\n')
    os.system('git log --oneline')
    print('\n')
    os.system('git push https://github.com/douglasdalves/sistema_python.git master')
    print('\n')
    #os.chdir('C:\scripts')
    #print ("Voce esta em: %s" % os.getcwd())
    print(colored('Processo Concluido, verifique no GitHub.', 'green', attrs=['bold']))
