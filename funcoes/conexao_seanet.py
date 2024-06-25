
from variaveis.interface_config import *


caminho_log_ping = Path("C:/scripts_logs")
caminho_fun_seanet = Path("C:/scripts")

LOG_PING = datetime.now().strftime('Ping-seanet_%d_%m_%Y_%H_%M_%S.log')

func_cabecalho('Ping para o IP da Seanet')
valor_ping = input('Digite a quantidade de ping desejada: ')
gerar_ping = subprocess.run(["ping", "-n", valor_ping, ping_seanet])
dados_pc()

# os.chdir(caminho_log_ping)
# os.system('ping -n 8 186.251.248.1 > ping.log')
# os.rename('ping.log', LOG_PING)
# os.chdir(caminho_fun_seanet)




