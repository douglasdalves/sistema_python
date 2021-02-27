import os

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
print('Lista o Repositorio remoto:')
os.system('git remote')

print('\n')
os.system('git status')

#os.system('git push server master')---
#------------------------------------------------
# Aplicar alteracoes

while True:
    print('\n')
    aplicar = str(input('Voce quer realizar as alteracoes? '))
    if aplicar == 'sim':
        print('\n')
        print('Certo vou aplicar o git add .')
        os.system('git add .')
        print('Agora precisa commitar, digite abaixo..')
        os.system(input())
        print('\n')
        os.system('git log')
    elif aplicar == 'enviar':
        print('Enviando dados ao Servidor')
        os.system('git push server master')
        print('\n')
    else:
        aplicar == 'nao'
        print('Tudo bem volte quando quiser')
        break

#------------------------------------------------
# dados padroes finais

print('\n')
os.system('echo Data do teste: %date%')
os.system('echo Hora do teste: %time%')
os.system('echo Equipamento testado: %computername%')
os.system('echo Usuario do windows: %username%')
print('\n')