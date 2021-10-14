#------------------------------------------------
#Importacao de dados

def linha_func(tam = 42):
    return '-' * tam

def func_cabecalho (txt):
    print('\n')
    print(linha_func())
    print(txt.center(42))
    print(linha_func())


import subprocess

func_cabecalho('Verificando o Acesso ao DNS do Google')
subprocess.run(["tracert", "-d", "-w", "2000", "dns.google"])

func_cabecalho('Consulta de DNS com Site')
print('\n')
subprocess.run(["nslookup"])

