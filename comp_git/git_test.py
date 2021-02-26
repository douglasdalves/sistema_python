import os

def linha(tam = 42):
    return '-' * tam

def cabecalho (txt):
    print('\n')
    print(linha())
    print(txt.center(42))
    print(linha())


cabecalho('Funcoes do GitHub')

os.chdir('C:\scripts')
#Altere o diretório de trabalho atual
print ("Voce esta em: %s" % os.getcwd())
#Retorna o diretório de trabalho atual

os.system('git status')


print('\n')
os.system('echo Data do teste: %date%')
os.system('echo Hora do teste: %time%')
os.system('echo Equipamento testado: %computername%')
os.system('echo Usuario do windows: %username%')
print('\n')