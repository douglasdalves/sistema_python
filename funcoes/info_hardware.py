import os

def linha(tam = 42):
    return '-' * tam

def cabecalho (txt):
    print(linha())
    print(txt.center(42))
    print(linha())


cabecalho('Informacoes da Placa Mae')
os.system('wmic baseboard get product,Manufacturer,version,serialnumber')

cabecalho('Informacoes de Rede')
print('\n')

print('Interfaces de REDE - Detalhes')
os.system(' /scripts/funcoes/interface_rede.ps1')

print('\n')
print('Dados foram carregados em nova aba.')


print('\n')
os.system('echo Data do teste: %date%')
os.system('echo Hora do teste: %time%')
os.system('echo Equipamento testado: %computername%')
os.system('echo Usuario do windows: %username%')
print('\n')

os.system('start C:\Windows\System32\cmd.exe /k %windir%\system32\ipconfig.exe')
os.system('start C:\Windows\System32\msinfo32.exe')