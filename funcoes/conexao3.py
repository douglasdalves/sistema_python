import os

def linha(tam = 42):
    return '-' * tam

def cabecalho (txt):
    print('\n')
    print(linha())
    print(txt.center(42))
    print(linha())


cabecalho('Smartphone Redmi k20')
os.system('ping -n 4 192.168.8.104')

cabecalho('Smartphone Mi 8 lite')
os.system('ping -n 4 192.168.8.105')
print('\n')
os.system('echo Data do teste: %date%')
os.system('echo Hora do teste: %time%')
os.system('echo Equipamento testado: %computername%')
os.system('echo Usuario do windows: %username%')
print('\n')