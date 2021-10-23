
import subprocess
import time
from termcolor import colored
from variaveis.interface_config import *


caminho_log_ping = r'C:/scripts_logs/logs_ping'
LOG_PING = datetime.now().strftime('Ping40seanet_%d_%m_%Y_%H_%M_%S.log')


func_cabecalho('Ping 40x para o IP da Seanet')
gerar_ping = subprocess.run(["ping", "-n", "40", ping_seanet])
dados_pc()
os.chdir(caminho_log_ping)
os.system('ping -n 40 186.251.248.1 > ping.log')
os.rename('ping.log', LOG_PING)



""" with open("ping40seanet.log", 'w') as arquivo:
    arquivo.write("imprime no arquivo")

with open("ping40seanet.log", 'r') as arquivo:
    print(arquivo.read()) """


#os.system('ping -n 40 186.251.248.1')
#os.system('ping -n 8 192.168.246.17') #ip da vpn
