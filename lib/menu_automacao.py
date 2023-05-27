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
t_menu5 = 'Processos Windows'
t_menu6 = 'Energy Report'

myfile_cp_logs = r'C:/scripts_logs'
myfile_energy_report = r'C:/sistema_python/funcoes_tarefas/energy-report.bat'
myfile_processos = r'C:/sistema_python/funcoes_tarefas/processos_wind.bat'

#------------------------------------------------
#Codigo do menu 4

def abrir_autom():
    while True:
        resposta = menu_secund([t_menu,t_menu1,t_menu2,t_menu3,t_menu4,t_menu5,t_menu6,opcao_captura,opcao_retorno])
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
            print('{}'.format(op6), 'Processos Windows')
            os.system('cls') or None
            os.startfile(myfile_processos)
        elif resposta == 7:
            print('{}'.format(op7), 'Energy Report')
            os.startfile(myfile_energy_report)
            sleep(35)            
            os.chdir(myfile_cp_logs)
            sleep(35)
            os.startfile('energy-report.html')
        elif resposta == 8:
            print('{}'.format(op7), 'Captura de Tela')
            gerar_print()
        elif resposta == 9:
            frase_retorno()
        else:
            leia_opcao()
            sleep(2)