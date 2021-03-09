#------------------------------------------------
#Importacao de dados

from lib.interface import *
#from time import sleep
import os
import sys
from termcolor import colored
import pyautogui
import subprocess

#------------------------------------------------
# configuracao de layout

def linha(tam = 42):
    return '-' * tam

def cabecalho (txt):
    print('\n')
    print(linha())
    print(txt.center(42))
    print(linha())


#------------------------------------------------
# configuracao da funcao
# tratativa de ping com assistente e chama sistema.py apos

cabecalho('Ping 80x para o IP da Seanet')
os.system('ping -n 80 186.251.248.1')
#os.system('ping 192.168.246.23 -t') #ip da vpn para test

print('\n')
os.system('echo Data do teste: %date%')
os.system('echo Hora do teste: %time%')
os.system('echo Equipamento testado: %computername%')
os.system('echo Usuario do windows: %username%')
print('\n')
#sleep(50)

#------------------------------------------------
# chamar o menu principal

import sistema
subprocess.run("sistema.py", shell=True)

#os.system('start sistema.py')
#subprocess.run([sys.executable, "sistema.py"])
#exec(open("sistema.py").read())

