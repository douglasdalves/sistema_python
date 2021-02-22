import os

def linha(tam = 42):
    return '-' * tam

def cabecalho (txt):
    print('\n')
    print(linha())
    print(txt.center(42))
    print(linha())
    print('\n')


cabecalho('Detalhes da versao do SO')
os.system('wmic os get buildnumber,caption,CSDVersion')
os.system('wmic OS get OSArchitecture')

os.system('echo Data do teste: %date%')
os.system('echo Hora do teste: %time%')
os.system('echo Equipamento testado: %computername%')
os.system('echo Usuario do windows: %username%')
print('\n')

os.system('winver')