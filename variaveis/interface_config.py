from termcolor import colored
from datetime import datetime
from time import sleep
from tqdm import tqdm
from pathlib import Path


import platform
import getpass
import pyautogui
import logging
import os
import subprocess
import time
import curses


#------------------------------------------------
#
# Configuração básica do logger

log_file = Path("C:/scripts_logs/log-app/log_aplication.txt")


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


#------------------------------------------------
# variaveis

espaco = print('\n')

myfile_captura = Path("C:/scripts_logs/captura/print_sistema.png")
myfile_local_captura = Path("C:/scripts_logs/captura")
myfile_bkp_pip = Path("C:/scripts_logs/info_pacotes/backupPIP_python.txt")

LOG_FILENAME = datetime.now().strftime('Print_aplic_%d_%m_%Y_%H_%M_%S.png')

#--------------------------------------------
#('Configuracoes do menu funcoes')

def func_cabecalho (txt):
    """
    -> Realiza a personalizacão de titulo
    : Abre uma linha de espaço
    : Printa uma linha em verde
    : Texto dentro das linhas
    """
    print('\n')
    print(colored('-' * 42, 'green'))
    print(txt.center(42))
    print(colored('-' * 42, 'green'))


#--------------------------------------------
# configuracao dados da maquina

def dados_pc():
    """
    -> Gera os dados de Data, Hora, Equipamento, Usuário
    : Coleta o datatime
    : Nome do equipamento
    : User do windows
    """
    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
    text_data = colored('Data e Hora do teste:', 'blue', attrs=['bold'])

    cpu = platform.node()
    text_cpu = colored('Equipamento do Teste:', 'blue', attrs=['bold'])

    user = getpass.getuser()
    text_user = colored('Usuario do Sistema:', 'blue', attrs=['bold'])

    print('\n','\n', '--------- Testes Concluidos ---------')
    print(f'{text_data} {data_e_hora_em_texto}')
    print(f'{text_cpu} {cpu}')
    print(f'{text_user} {user}', '\n')


#--------------------------------------------
# variaveis das funcoes conexao

ping_seanet = '186.251.248.1'


#--------------------------------------------
## configuracoes das opcoes


#----# Captura de tela (print)
opcao_captura = colored('Captura de Tela', 'red')

def gerar_print():
    """
    -> Trabalha com a geracao de print e salvar o mesmo
    : Avisa sobre a captura
    : Realiza a captura
    : Salva no local informado
    : Troca de diretorio
    : Renomeia o arquivo
    """
    print('\n', '-- Captura de Tela -- ')
    print('Print gerado em Scripts_logs', '\n')
    capturar = pyautogui.screenshot()
    capturar.save(myfile_captura)
    os.chdir(myfile_local_captura)
    os.rename('print_sistema.png', LOG_FILENAME)


#---# ('Retornando para o menu principal')

fra1 = colored('Retornando para o menu principal', 'yellow', attrs=['bold'])

def retorno(txt):
    print(linha())
    print(txt.center(53))
    print(linha())
    print('\n')

opcao_retorno = colored('Retornar ao Home', 'blue')

def frase_retorno():
    os.system('cls') or None
    retorno('{}'.format(fra1))
    exec(open("sistema.py").read())


#---# funcao sair
def funcao_sair():
    """
    -> Funcao de sair da aplicacao do python
    : Abre espaco antes e depois da mensagem
    : Mensagem de aviso
    : Time para visualizar o processo
    : Parametro de sair - closed
    """
    print('\n')
    cabecalho_sup('Saindo do sistema... Até logo')
    print('\n')
    sleep(2)
    os.close()


#--------------------------------------------
#('Configuracoes do menu inicial')


# Função para criar uma linha de separação
def linha(tam=42):
    return '-' * tam

# Função para exibir o cabeçalho do menu
def cabecalho_sup(txt):
    print(linha())
    print(colored(txt.center(42), 'cyan', attrs=['bold']))
    print(linha())

# Função para exibir o cabeçalho inferior do menu
def cabecalho_inf(txt):
    print(linha())
    print(colored(txt.center(42), 'green'))


# Função para exibir o menu e capturar a escolha do usuário
def menu(options, title):
    cabecalho_sup(title)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    cabecalho_inf('Escolha uma opção:')
    while True:
        try:
            choice = int(input())
            if 1 <= choice <= len(options):
                return choice
            else:
                print(colored('Opção inválida. Tente novamente.', 'red'))
        except ValueError:
            print(colored('ERRO: Por favor, digite um número inteiro válido.', 'red'))


#--------------------------------------------

def leia_opcao():
    print(colored('ERRO! Digite uma opção valida!','magenta'))
