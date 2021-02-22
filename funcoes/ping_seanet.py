import os
from time import sleep

def linha(tam = 42):
    return '-' * tam

def cabecalho (txt):
    print('\n')
    print(linha())
    print(txt.center(42))
    print(linha())

cabecalho('Ping 80x para o IP da Seanet')
os.system('ping -n 80 186.251.248.1')
#os.system('ping 192.168.246.23 -t') #ip da vpn para test

print('\n')
os.system('echo Data do teste: %date%')
os.system('echo Hora do teste: %time%')
os.system('echo Equipamento testado: %computername%')
os.system('echo Usuario do windows: %username%')
print('\n')
sleep(50)
