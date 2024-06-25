import os
import subprocess
from termcolor import colored
from variaveis.interface_config import *


#--------------------------------------------

myfile_pacote = r'C:/sistema_python/automacao_sh/altera_pacote.sh'

# configuracoes do menu

def opcoes_pacotes():
    func_cabecalho('Lista os Pacotes do Python')
    print('\n')
    subprocess.run(["pip", "list",])
    os.system('pip list > C:/scripts_logs/info_pacotes/backupPIP_python.txt')
    sleep(15)

func_cabecalho('Pacotes do Python')

#------------------------------------------------
# chamar a instalacao de pacotes


aplicar = 0
while aplicar != 3:
    print('''Funcoes: 
    [1] Validar pacotes
    [2] Instalar ou atualizar
    [3] Voltar ao menu anterior''')
    print('\n')
    aplicar = str(input('Escolha uma opcao: '))
    if aplicar == '1':
        print('\n')
        opcoes_pacotes()
        os.startfile(myfile_pacote)
        print('\n')
    elif aplicar == '2':
        print('\n')
        exec(open("pacotes_config.bat").read())
        print('\n')
    else:
        aplicar == '3'
        func_cabecalho('Tudo bem volte quando quiser')
        break


dados_pc()
