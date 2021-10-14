
import os
import subprocess
import time

myfile_sistema = r'C:/scripts'

#---------------------------------------------------

def func_pull():
    print('Baixando os dados do repositorio')
    print('\n')
    os.system('rm -rf scripts')
    print('\n')

    #os.chdir('C:')

    os.system('git pull https://github.com/douglasdalves/sistema_python.git scripts')
    time.sleep(10)

    print('\n')
    os.listdir('scripts')
    print('\n')
    os.chdir(myfile_sistema)
    os.system('git log --oneline')
    os.startfile(sistema.py)

#---------------------------------------------------


def menu_pull():
    aplicar = 0
    while aplicar != 5:
        print('''Opcoes:
        [1] Não executar
        [2] Start do git pull
        [3] ok''')
        print('\n')
        aplicar = str(input('Digite uma opcao? '))
        if aplicar == '1':
            print('Tudo bem volte quando quiser')
            break
        if aplicar == '2':
            func_pull()
        else:
            aplicar == '3'

menu_pull()

