import os
import subprocess
from termcolor import colored
from funcoes.interface_test import *


func_cabecalho('Ping 40x para o IP da Seanet')
subprocess.run(["ping", "-n", "40", "186.251.248.1"])
#os.system('ping -n 40 186.251.248.1')
#os.system('ping -n 8 192.168.246.17') #ip da vpn
dados_pc()