#------------------------------------------------
#Importacao de dados

from variaveis.interface_config import *
from automacao_sh import *
from time import sleep

#https://docs.microsoft.com/pt-br/windows/wsl/filesystems#:~:text=Execute%20bin%C3%A1rios%20do%20Linux%20no,.exe%20).&text=Bin%C3%A1rios%20invocados%20desta%20maneira%3A,como%20usu%C3%A1rio%20padr%C3%A3o%20do%20WSL.

#------------------------------------------------
#Linhas de personalizacao

myfile_docker = r'C:/sistema_python/automacao_sh/wsl_start_docker.sh'
myfile_stop = r'C:/sistema_python/automacao_sh/wsl_stop_docker.sh'

myfile_docker1 = r'C:/sistema_python/automacao_sh'

#------------------------------------------------
# funções

def wsl_status():
    print('\n')
    subprocess.run(["wsl", "-l", "-v"])
    print('\n')

# Dados menu
t_menu = 'Status da WSL'
t_menu1 = 'Iniciando o WSL2'
t_menu2 = 'Stop do WSL2'
t_menu3 = 'Start docker - test'
t_menu4 = 'Stop docker - test'

#------------------------------------------------
#Codigo do menu 6

def abrir_wsl():
    while True:
        resposta = menu_secund([t_menu,t_menu1,t_menu2,t_menu3,t_menu4,opcao_captura, opcao_retorno])
        if resposta == 1:
            os.system('cls') or None
            print('{}'.format(op1), 'Status do WSL2')
            wsl_status()
        elif resposta == 2:
            os.system('cls') or None
            print('{}'.format(op2), 'Start WSL2')
            print('\n')
            os.system('wsl ~ --distribution Ubuntu --user root')
            sleep(2)
            os.system('Start Ubuntu')
            #os.system('exit')
            print('\n', 'Status do Subsistema')
            wsl_status()
        elif resposta == 3:
            print('{}'.format(op3), 'Stop do Subsistema WS2')
            print('\n','Stop da WSL2','\n')
            os.system('wsl --shutdown && wsl -l -v')
            #sleep(2)
            #wsl_status()
        elif resposta == 4:
            print('{}'.format(op4), 'Teste Start Docker')
            subprocess.run(myfile_docker, shell=True)
            os.system('wsl docker ps')
        elif resposta == 5:
            print('{}'.format(op4), 'Test Stop Docker')
            #os.chdir(myfile_docker1)
            os.system('wsl docker ps')
            subprocess.run(myfile_stop, shell=True)
            os.system('wsl docker ps')
        elif resposta == 6:
            print('{}'.format(op5), 'Captura de Tela')
            gerar_print()
        elif resposta == 7:
            print('{}'.format(op6), 'Retorno do Menu')
            frase_retorno()
        else:
            leia_opcao()
            sleep(2)