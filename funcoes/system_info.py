import os

def linha(tam = 42):
    return '-' * tam

def cabecalho (txt):
    print('\n')
    print(linha())
    print(txt.center(42))
    print(linha())
    print('\n')


cabecalho('Informacoes do Windows')
os.system('systeminfo')

os.system('echo Data do teste: %date%')
os.system('echo Hora do teste: %time%')
os.system('echo Equipamento testado: %computername%')
os.system('echo Usuario do windows: %username%')
print('\n')