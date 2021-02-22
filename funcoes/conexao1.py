import os

def linha(tam = 42):
    return '-' * tam

def cabecalho (txt):
    print('\n')
    print(linha())
    print(txt.center(42))
    print(linha())


cabecalho('Smart TV - LG')
os.system('ping -n 3 192.168.8.103')

cabecalho('Echo Dot - Alexa')
os.system('ping -n 3 192.168.8.107')

cabecalho('Smart plug 1')
os.system('ping -n 3 192.168.8.108')

cabecalho('Smart plug 2')
os.system('ping -n 3 192.168.8.109')

print('\n')
os.system('echo Data do teste: %date%')
os.system('echo Hora do teste: %time%')
os.system('echo Equipamento testado: %computername%')
os.system('echo Usuario do windows: %username%')
print('\n')