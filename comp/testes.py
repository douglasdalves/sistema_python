import os
import sys
from termcolor import colored

def linha_igual(tam = 42):
    return '=' * tam

def retorno (txt):
    print(linha_igual())
    print(txt.center(42))
    print(linha_igual())
    print('\n')

def frase_retorno():
    retorno('Retornando para o menu principal')


frase_retorno()
#retorno('Retornando para o menu principal')
#retorno(colored('Retornando para o menu principal', 'white', 'on_red'))

