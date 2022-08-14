import os
from termcolor import colored
import subprocess
from variaveis.interface_config import *
from comp_git.git_funcoes import *


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
        func_commit()
    elif aplicar == '2':
        print(espaco)
    elif aplicar == '3':
        func_github()
    else:
        aplicar == 'nao'
        cabecalho_git('Tudo bem volte quando quiser')
        os.system('git log --oneline')
        break


#------------------------------------------------
# dados padroes finais

dados_pc()

#https://pt.stackoverflow.com/questions/6188/como-copiar-commits-de-um-branch-para-o-outro