#------------------------------------------------
#Importacao de dados

from lib.aplicacao_interface import *
from time import sleep
import os
import pyautogui
import subprocess


#------------------------------------------------


#------------------------------------------------
#Codigo do menu 5

while True:
    resposta = menu(['Pacotes do Python','GitHub','DevOps','Variavel Ambiente','Test_02','Test_03','Captura de Tela','Retornar ao Home'])
    if resposta == 1:
        os.system('cls') or None
        print('Opcao 1 - Info de Pacotes')
        exec(open("./funcoes_tarefas/pacotes_detalhes.py").read())
    elif resposta == 2:
        print('Opcao 2 - Infos em GitHub')
        os.system('cls') or None
        exec(open("./comp_git/git_test.py").read())
    elif resposta == 3:
        print('Opcao 3 - Infos em DevOps')
        os.system('cls') or None
        exec(open("./funcoes_tarefas/func_devops.py").read())
    elif resposta == 4:
        print('Opcao 4 - Variaveis de Ambiente')
        os.system('cls') or None
        exec(open("./funcoes_tarefas/func_variavel.py").read())
    elif resposta == 5:
        print('Opcao 5 - test1')
    elif resposta == 6:
        print('Opcao 6 - test2')
    elif resposta == 7:
        print('Opcao 7 - Captura de Tela')
        gerar_print_aplicacao()
    elif resposta == 8:
        frase_retorno()
    else:
        leia_opcao()
        sleep(2)