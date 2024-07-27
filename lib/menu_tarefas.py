#------------------------------------------------
#Importacao de dados

from funcoes_tarefas.func_devops import func_devops
from variaveis.interface_config import *
from comp_git.git_test import *

#------------------------------------------------

myfile_programas = Path("C:/sistema_python/funcoes_tarefas/instal_programas.bat")

# Dados menu
t_menu = 'Pacotes do Python'
t_menu1 = 'GitHub'
t_menu2 = 'DevOps'
t_menu3 = 'Variavel Ambiente'
t_menu4 = 'Install Programas'

#------------------------------------------------
#Codigo do menu 2

def abrir_taref():
    while True:
        resposta = menu_secund([t_menu,t_menu1,t_menu2,t_menu3,t_menu4,opcao_captura,opcao_retorno])
        if resposta == 1:
            os.system('cls') or None
            print('{}'.format(op1), 'Info de Pacotes')
            exec(open("./funcoes_tarefas/pacotes_detalhes.py").read())
        elif resposta == 2:
            print('{}'.format(op2), 'Infos em GitHub')
            os.system('cls') or None
            notas_git()
        elif resposta == 3:
            print('{}'.format(op3), 'Infos em DevOps')
            os.system('cls') or None
            func_devops()
        elif resposta == 4:
            print('{}'.format(op4), 'Variaveis de Ambiente')
            os.system('cls') or None
            exec(open("./funcoes_tarefas/func_variavel.py").read())
        elif resposta == 5:
            print('{}'.format(op5), 'Instacao de Progrmas via CHOCO')
            os.system('cls') or None
            os.startfile(myfile_programas)
        elif resposta == 6:
            print('{}'.format(op6), 'Captura de Tela')
            gerar_print()
        elif resposta == 7:
            frase_retorno()
        else:
            leia_opcao()
            sleep(2)