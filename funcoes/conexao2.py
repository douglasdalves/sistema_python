import sys
import subprocess
from termcolor import colored
from funcoes.interface_test import *


#--------------------------------------------
# configuracoes do menu

func_cabecalho('Notebook Douglas')
subprocess.run(["ping", "-n", "4", "192.168.8.101"])

func_cabecalho('Notebook Marcia')
subprocess.run(["ping", "-n", "4", "192.168.8.102"])
dados_pc()

