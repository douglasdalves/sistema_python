import sys
import os
import subprocess
from termcolor import colored
from datetime import datetime
import platform
import getpass

import pyautogui
from time import sleep
from tqdm import tqdm

#------------------------------------------------
# variaveis

espaco = print('\n')

myfile_saindo = r'C:/scripts/funcoes/saindo_sistema.py'

myfile_captura = r'C:/scripts_logs/captura/print_sistema.png'
myfile_local_captura = r'C:/scripts_logs/captura'
LOG_FILENAME = datetime.now().strftime('Print_aplic_%d_%m_%Y_%H_%M_%S.png')

myfile_bkp_pip = r'C:/scripts_logs/info_pacotes/backupPIP_python.txt'


#--------------------------------------------
# variaveis das funcoes conexao

ping_seanet = '186.251.248.1'
ping_roteador = '192.168.8.1'
ping_tv = '192.168.8.103'

ping_alexa = '192.168.8.107'
ping_dot4 = '192.168.8.114'

ping_plug1 = '192.168.8.108'
ping_plug2 = '192.168.8.109'
ping_sonoff1 = '192.168.8.112'
ping_sonoff2 = '192.168.8.116'

ping_lampada = '192.168.8.110'
ping_lampada2 = '192.168.8.115'
ping_fita_led = '192.168.8.117'

ping_controle = '192.168.8.111'

ping_acer = '192.168.8.101'
ping_not_mor = '192.168.8.102'
ping_pc = '192.168.8.106'
ping_dell = '192.168.8.113'

ping_mi9 = '192.168.8.104'
ping_mi8 = '192.168.8.105'


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


#-----------------------------------------------------

# anotacao da config de data e hora

#---%d - O dia do mês representado por um número decimal (de 01 a 31)
#---%m - O mês representado por um número decimal (de 01 a 12)
#---%Y - O ano representado por um número decimal incluindo o século
#---%H - A hora representada por um número decimal usando um relógio de 24 horas (de 00 a 23)
#---%M - O minuto representado por um número decimal (de 00 a 59)



#-----------------------------------------------------
# Dados dos Menus (opcao)

op1 = 'Opcao 1 - '
op2 = 'Opcao 2 - '
op3 = 'Opcao 3 - '
op4 = 'Opcao 4 - '
op5 = 'Opcao 5 - '
op6 = 'Opcao 6 - '
op7 = 'Opcao 7 - '
op8 = 'Opcao 8 - '

#--------------------------------------------
## configuracoes das mensagens

def leiaInt(msg):
    """
    -> Apresenta as mensagens de erro ao usar o menu incorretamente
    : Le a entrada
    : valida a entrada
    : Retorna a mensagem adequada
    : Trabalha com a cor vermelha
    """
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(colored('ERRO: Por favor, digite um numero inteiro valido.','red'))
            continue
        except (KeyboardInterrupt):
            print(colored('Usuario preferiu não digitar esse numero.','red'))
            return 0
        else:
            return n

def leia_opcao():
    print(colored('ERRO! Digite uma opção valida!','magenta'))

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

#frase_retorno = 'Retornando para o menu principal'
fra1 = colored('Retornando para o menu principal', 'yellow', attrs=['bold'])

def retorno (txt):
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


#print(colored(txt.center(42), 'red', attrs=['bold']))

def linha(tam = 42): ## usado por outros menus
    return '-' * tam

def cabecalho_sup (txt):
    print(linha())
    print(colored(txt.center(42),'cyan',attrs=['bold']))
    print(linha())

def cabecalho_inf (txt):
    print(linha())
    print(colored(txt.center(42),'green'))

def menu(lista):
    cabecalho_sup('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    cabecalho_inf('Escolha uma Opção')
    print(linha())
    opc = leiaInt("\nSua Opção: ")
    return opc

#cabecalho_sup(colored('MENU PRINCIPAL','cyan',attrs=['bold']))
#cabecalho_sup('MENU PRINCIPAL')


#--------------------------------------------
#('Configuracoes dos menus secudarios')

def cabeçalho (txt):
    print('-' * 42)
    print(colored(txt.center(42),'magenta'))
    print('-' * 42)

def menu_secund(lista):
    cabeçalho('Testes secundários')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print('-' * 42)
    opc = leiaInt("\nSua Opção: ")
    return opc


#--------------------------------------------
