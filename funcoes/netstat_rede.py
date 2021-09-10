import os
from time import sleep

def linha(tam = 42):
    return '-' * tam

def cabecalho (txt):
    print('\n')
    print(linha())
    print(txt.center(42))
    print(linha())
    print('\n')


cabecalho('Testando a Rede em Netstat')
os.system('Netstat')
sleep(80)