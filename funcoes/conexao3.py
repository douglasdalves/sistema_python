import sys
import subprocess
from termcolor import colored
from funcoes.interface_test import *


#--------------------------------------------
# configuracoes do menu

func_cabecalho('Smartphone Redmi k20')
subprocess.run(["ping", "-n", "4", "192.168.8.104"])

func_cabecalho('Smartphone Mi 8 lite')
subprocess.run(["ping", "-n", "4", "192.168.8.105"])
dados_pc()
