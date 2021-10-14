
import subprocess
import time
from termcolor import colored
from variaveis.interface_config import *


func_cabecalho('Ping 40x para o IP da Seanet')
gerar_ping = subprocess.run(["ping", "-n", "40", ping_seanet])
dados_pc()



""" with open("ping40seanet.log", 'w') as arquivo:
    arquivo.write("imprime no arquivo")

with open("ping40seanet.log", 'r') as arquivo:
    print(arquivo.read()) """


#os.system('ping -n 40 186.251.248.1')
#os.system('ping -n 8 192.168.246.17') #ip da vpn
