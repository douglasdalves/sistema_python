import os

def linha(tam = 42):
    return '-' * tam

def cabecalho (txt):
    print('\n')
    print(linha())
    print(txt.center(42))
    print(linha())


cabecalho('Notebook Douglas')
os.system('ping -n 4 192.168.8.101')

cabecalho('Notebook Marcia')
os.system('ping -n 4 192.168.8.102')
print('\n')
os.system('echo Data do teste: %date%')
os.system('echo Hora do teste: %time%')
os.system('echo Equipamento testado: %computername%')
os.system('echo Usuario do windows: %username%')
print('\n')