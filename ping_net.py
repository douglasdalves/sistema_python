#------------------------------------------------
#Importacao de dados

import subprocess
from termcolor import colored
from variaveis.interface_config import *
#from time import sleep

#------------------------------------------------
# configuracao da funcao
# tratativa de ping com assistente e chama sistema.py apos

func_cabecalho('Ping 80x para o IP da Seanet')
subprocess.run(["ping", "-n", "80", "186.251.248.1"])
#os.system('ping 192.168.246.23 -t') #ip da vpn para test

dados_pc()
#sleep(50)

#------------------------------------------------
# chamar o menu principal

import sistema
subprocess.run("sistema.py", shell=True)

#os.system('start sistema.py')
#subprocess.run([sys.executable, "sistema.py"])
#exec(open("sistema.py").read())

