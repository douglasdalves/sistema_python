
import subprocess
from termcolor import colored
from variaveis.interface_config import *
import logging



log_file = 'C:/scripts_logs/log_aplication.txt'

logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(filename=log_file, level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(filename=log_file, level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

# Mensagens de diferentes níveis
logging.info('Esta é uma mensagem informativa.')
logging.debug('Esta é uma mensagem de debug.')
logging.warning('Esta é uma mensagem de aviso.')
logging.error('Esta é uma mensagem de erro.')
logging.critical('Esta é uma mensagem crítica.')


caminho_log_ping = r'C:/scripts_logs'
caminho_fun_seanet = r'C:/scripts'
LOG_PING = datetime.now().strftime('Ping-seanet_%d_%m_%Y_%H_%M_%S.log')

func_cabecalho('Ping para o IP da Seanet')
valor_ping = input('Digite a quantidade de ping desejada: ')
gerar_ping = subprocess.run(["ping", "-n", valor_ping, ping_seanet])
dados_pc()

# os.chdir(caminho_log_ping)
# os.system('ping -n 8 186.251.248.1 > ping.log')
# os.rename('ping.log', LOG_PING)
# os.chdir(caminho_fun_seanet)




