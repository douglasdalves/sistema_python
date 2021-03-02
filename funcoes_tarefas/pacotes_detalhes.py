import os

def linha(tam = 42):
    return '-' * tam

def cabecalho (txt):
    print('\n')
    print(linha())
    print(txt.center(42))
    print(linha())
    print('\n')


cabecalho('Lista os Pacotes do Python')
os.system('pip list')

cabecalho('Instalar Pacotes do Python')


print('\n')
os.system('echo Data do teste: %date%')
os.system('echo Hora do teste: %time%')
os.system('echo Equipamento testado: %computername%')
os.system('echo Usuario do windows: %username%')
print('\n')

#os.system('start C:\Windows\System32\cmd.exe /k %windir%\system32\ipconfig.exe')
#os.system(' /scripts/funcoes/interface_rede.ps1')