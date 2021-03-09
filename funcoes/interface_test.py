import sys
import subprocess
from termcolor import colored
from datetime import datetime
import platform
import getpass


#--------------------------------------------
#('Configuracoes do menu')

def linha_func(tam = 42):
    return '-' * tam

def func_cabecalho (txt):
    print('\n')
    print(linha_func())
    print(txt.center(42))
    print(linha_func())

#--------------------------------------------
# configuracao dados da maquina

def dados_pc():
    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
    text_data = colored('Data e Hora do teste:', 'blue', attrs=['bold'])

    cpu = platform.node()
    text_cpu = colored('Equipamento do Teste:', 'blue', attrs=['bold'])

    user = getpass.getuser()
    text_user = colored('Usuario do Sistema:', 'blue', attrs=['bold'])

    print('\n')
    print('--------- Testes Concluidos ---------')
    print(f'{text_data} {data_e_hora_em_texto}')
    print(f'{text_cpu} {cpu}')
    print(f'{text_user} {user}')
    print('\n')



#-----------------------------------------------------

# anotacao da config de data e hora

#---%d - O dia do mês representado por um número decimal (de 01 a 31)
#---%m - O mês representado por um número decimal (de 01 a 12)
#---%Y - O ano representado por um número decimal incluindo o século
#---%H - A hora representada por um número decimal usando um relógio de 24 horas (de 00 a 23)
#---%M - O minuto representado por um número decimal (de 00 a 59)

#-----------------------------------------------------