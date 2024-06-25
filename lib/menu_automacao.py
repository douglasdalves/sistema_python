#------------------------------------------------
#Importacao de dados

from variaveis.interface_config import *
from funcoes.info_hardware import *

#------------------------------------------------
#Linhas de personalizacao

# Dados menu
t_menu = 'Versao do Windows'
t_menu1 = 'Detalhes do Windows'
t_menu2 = 'Informacao do Hardware'
t_menu3 = 'Rotas do Windows'
t_menu4 = 'Processos Windows'

myfile_cp_logs = Path("C:/scripts_logs")
myfile_processos = Path("C:/sistema_python/funcoes_tarefas/processos_wind.bat")

#------------------------------------------------
#Codigo do menu 4

def abrir_autom():
    while True:
        resposta = menu_secund([t_menu,t_menu1,t_menu2,t_menu3,t_menu4,opcao_captura,opcao_retorno])
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
            print('{}'.format(op4), 'Rotas do Windows')
            route()
        elif resposta == 5:
            print('{}'.format(op5), 'Processos Windows')
            os.system('cls') or None
            os.startfile(myfile_processos)
        elif resposta == 6:
            print('{}'.format(op6), 'Captura de Tela')
            gerar_print()
        elif resposta == 7:
            frase_retorno()
        else:
            leia_opcao()
            sleep(2)