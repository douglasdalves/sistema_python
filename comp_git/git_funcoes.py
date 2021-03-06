import os
from termcolor import colored
import sys
import subprocess
#from lib.aplicacao_interface import *
from funcoes.interface_test import *

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
    os.system('git checkout dev')
    print('\n')
    print('Certo vou aplicar o git add .')
    os.system('git add .')
    print('\n')
    print('Agora precisa commitar, digite abaixo..')
    print('ex: git commit -m "msg"')
    print('\n')
    os.system(input())
    print('\n')
    os.system('git log --oneline')

def func_server():
    print('Enviando ao Servidor local')
    print('\n')
    os.system('git checkout master')
    print(colored('Voce esta na branch:', 'blue', attrs=['bold']))
    os.system('git branch')
    print('\n')
    os.system('git merge dev')
    os.system('git push server_sistema master')
    print('\n')
    os.system('git log --oneline')
    print('\n')
    os.chdir('C:\sistema_git') #Altere o diretório de trabalho atual
    print ("Voce esta em: %s" % os.getcwd()) #Retorna o diretório de trabalho atual
    os.system('git log --oneline')
    os.chdir('C:\scripts')
    print('\n')
    os.system('git log --oneline')
    os.system('git checkout dev')

def func_github():
    print('\n')
    print('Enviando dados ao Git Hub')
    os.chdir('C:\sistema_git') #Altere o diretório de trabalho atual
    print ("Voce esta em: %s" % os.getcwd()) #Retorna o diretório de trabalho atual
    print('\n')
    os.system('git log --oneline')
    print('\n')
    os.system('git push https://github.com/douglasdalves/sistema_python.git master')
    print('\n')
    os.chdir('C:\scripts')
    print ("Voce esta em: %s" % os.getcwd())
    print(colored('Processo Concluido, verifique no GitHub.', 'green', attrs=['bold']))

def func_pull():
    print('Baixando os dados do repositorio')
    print('\n')
    os.system('git log --oneline')
    os.chdir('C:')
    print('\n')
    os.system('git pull https://github.com/douglasdalves/sistema_python.git scripts')
    print('\n')
    os.system('git log --oneline')