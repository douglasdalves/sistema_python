import os
from termcolor import colored
import sys
import subprocess
#from lib.aplicacao_interface import *
from funcoes.interface_test import *

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
os.system('git log --oneline')
#subprocess.run(["git", "log", "--graph"])

#os.system('git push server master')---
#------------------------------------------------
# Aplicar alteracoes

while True:
    cabecalho_git('Funcoes: 1-Commit  2-Enviar_Server 3-GitHub')
    print('Opcao para sair, digite: Nao')
    aplicar = str(input('Voce quer realizar as alteracoes? '))
    if aplicar == '1':
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
    elif aplicar == '2':
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
    elif aplicar == '3':
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
    else:
        aplicar == 'nao'
        cabecalho_git('Tudo bem volte quando quiser')
        os.system('git log --oneline')
        break


#------------------------------------------------
# dados padroes finais

dados_pc()