import os
from termcolor import colored
import sys

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

cabecalho('Funcoes do GitHub')

os.chdir('C:\scripts') #Altere o diretório de trabalho atual
print ("Voce esta em: %s" % os.getcwd()) #Retorna o diretório de trabalho atual

print(colored('Lista o Repositorio remoto:', 'blue', attrs=['bold']))
os.system('git remote -v')

print(colored('Lista as branches:', 'blue', attrs=['bold']))
os.system('git branch')

print('\n')
os.system('git status')

print('\n')
os.system('git log --graph')

#os.system('git push server master')---
#------------------------------------------------
# Aplicar alteracoes

while True:
    cabecalho('Funcoes: 1-Commit  2-Enviar_Server 3-GitHub')
    aplicar = str(input('Voce quer realizar as alteracoes? '))
    if aplicar == '1':
        print('\n')
        os.system('git checkout upgrade')
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
        print('Enviando dados ao Servidor')
        os.system('git push server_sistema master')
        print('\n')
        os.chdir('C:\sistema_git') #Altere o diretório de trabalho atual
        print ("Voce esta em: %s" % os.getcwd()) #Retorna o diretório de trabalho atual
        os.system('git log')
        os.chdir('C:\scripts')
    elif aplicar == '3':
        print('Enviando dados ao Servidor')
        os.system('')
        print('\n')
    else:
        aplicar == 'nao'
        cabecalho('Tudo bem volte quando quiser')
        break

#------------------------------------------------
# dados padroes finais

os.system('echo Data do teste: %date%')
os.system('echo Hora do teste: %time%')
os.system('echo Equipamento testado: %computername%')
os.system('echo Usuario do windows: %username%')
print('\n')