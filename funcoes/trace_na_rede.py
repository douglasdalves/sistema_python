import os

def linha(tam = 42):
    return '-' * tam

def cabecalho (txt):
    print(linha())
    print(txt.center(42))
    print(linha())


cabecalho('Excutando um Traceroute na Seanet')
os.system('tracert 186.251.248.1')

cabecalho('Excutando um Pathping na Seanet')
os.system('pathping 186.251.248.1')

print('\n')
os.system('echo Data do teste: %date%')
os.system('echo Hora do teste: %time%')
os.system('echo Equipamento testado: %computername%')
os.system('echo Usuario do windows: %username%')
print('\n')