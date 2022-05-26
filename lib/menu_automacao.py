#------------------------------------------------
#Importacao de dados

from variaveis.interface_config import *
#from funcoes.infos_windows import *
from funcoes.info_hardware import *
from time import sleep
import os


#------------------------------------------------
#Linhas de personalizacao

# Dados menu
t_menu = 'Versao do Windows'
t_menu1 = 'Detalhes do Windows'
t_menu2 = 'Informacao do Hardware'
t_menu3 = 'Relatorio de bateria'
t_menu4 = 'Rotas do Windows'
t_menu5 = 'Testes2'


#------------------------------------------------
#Codigo do menu 4

def abrir_autom():
    while True:
        resposta = menu_secund([t_menu,t_menu1,t_menu2,t_menu3,t_menu4,t_menu5,opcao_captura,opcao_retorno])
        if resposta == 1:
            os.system('cls') or None
            print('{}'.format(op1), 'Detalhes da Build do SO')
            versao_windows()
        elif resposta == 2:
            print('{}'.format(op2), 'Detalhes do HardWare')
            os.system('cls') or None
            system_info()
        elif resposta == 3:
            print('{}'.format(op3), 'Info de Hardware')
            info_hardware()
        elif resposta == 4:
            print('Opcao 4')
            os.system('cls') or None
        elif resposta == 5:
            print('{}'.format(op5), 'Rotas do Windows')
            route()
        elif resposta == 6:
            print('{}'.format(op6), 'test2')
        elif resposta == 7:
            print('{}'.format(op7), 'Captura de Tela')
            gerar_print()
        elif resposta == 8:
            frase_retorno()
        else:
            leia_opcao()
            sleep(2)