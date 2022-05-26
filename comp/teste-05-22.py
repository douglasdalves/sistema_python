from termcolor import colored
import subprocess

def func_cabecalho (txt):
    """
    -> Realiza a personalizacão de titulo
    : Abre uma linha de espaço
    : Printa uma linha em verde
    : Texto dentro das linhas
    """
    print('\n')
    print(colored('-' * 42, 'green'))
    print(txt.center(42))
    print(colored('-' * 42, 'green'))

fz = ['Smartphone Redmi k20','este']
import os

def ping_telefones():
    os.system('cls') or None
    r = dict()
    r[subprocess.run(["ping", "-n", "4", "192.168.8.101"])] = func_cabecalho('Smartphone Redmi k20')


ping_telefones()
help(func_cabecalho)