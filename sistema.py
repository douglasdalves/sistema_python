#------------------------------------------------
#Importacao de dados

from variaveis.interface_config import *
from time import sleep
import os
from termcolor import colored


#------------------------------------------------
#Codigo do menu principal

while True:
    resposta = menu(['Testes de Conexao','Agilizando Tarefas','Test de Rede','Testes Automatizados','Testes de Monitoracao','Tarefas em WSL','Pull do GitHub','Captura de Tela','Sair'])
    if resposta == 1:
        print('Opcao 1')
        os.system('cls') or None
        #os.system('test.bat')
        exec(open("./funcoes/conexao_seanet.py").read())
    elif resposta == 2:
        print('Opcao 2')
        os.system('cls') or None
        exec(open("./lib/menu_tarefas.py").read())
    elif resposta == 3:
        print('Opcao 3')
        os.system('cls') or None
        exec(open("./lib/menu_avancado.py").read())
    elif resposta == 4:
        print('Opcao 4 - Validacao Automatizada')
        os.system('cls') or None
        exec(open("./lib/menu_automacao.py").read())
    elif resposta == 5:
        print('Opcao 5 - Monitoracao da conexao')
        os.system('cls') or None
        exec(open("./lib/menu_aplicacao.py").read())
    elif resposta == 6:
        print('Opcao 6')
        os.system('cls') or None
        exec(open("./lib/menu_wsl.py").read())
    elif resposta == 7:
        func_pull()
    elif resposta == 8:
        gerar_print()
    elif resposta == 9:
        funcao_sair()
    else:
        leia_opcao()
        sleep(2)
    

#sts = os.system("mycmd" + " myarg")
# becomes
#retcode = call("mycmd" + " myarg", shell=True)