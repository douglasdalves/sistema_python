import os

def linha(tam = 42):
    return '-' * tam

def cabecalho (txt):
    print('\n')
    print(linha())
    print(txt.center(42))
    print(linha())

os.system('start C:\scripts\funcoes\conexao_seanet.py')
cabecalho('Ping 40x para o IP da Seanet')
os.system('ping -n 40 186.251.248.1')
#os.system('ping -n 8 192.168.246.17') #ip da vpn


print('\n')
os.system('echo Data do teste: %date%')
os.system('echo Hora do teste: %time%')
os.system('echo Equipamento testado: %computername%')
os.system('echo Usuario do windows: %username%')
print('\n')