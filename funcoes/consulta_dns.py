#------------------------------------------------
#Importacao de dados

from variaveis.interface_config import func_cabecalho
from variaveis.interface_config import dados_pc

import subprocess

func_cabecalho('Verificando o Acesso ao DNS do Google')
subprocess.run(["tracert", "-d", "-w", "2000", "dns.google"])

func_cabecalho('Consulta de DNS com Site')
print('\n')
subprocess.run(["nslookup"])

dados_pc()
print('\n')
