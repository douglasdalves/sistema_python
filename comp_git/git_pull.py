

from asyncio import sleep
import os
import subprocess
import time

myfile_sistema = r'C:/'
myfile_scripts_logs = r'C:/scripts_logs/scripts/'

#---------------------------------------------------

def func_pull():
    print('Atualizando os dados do repositorio', '\n')
    print ("Voce esta em: %s" % os.getcwd())
    print('\n')
    os.system('ls -ltr')
    os.system('rm -rf scripts')
    time.sleep(2)
    os.system('ls -ltr')
    print('\n')

    os.system('git clone https://github.com/douglasdalves/sistema_python.git scripts')

    print('Pasta atualizada, copiando os dados...', '\n')
    os.chdir(myfile_sistema)
    print ("Voce esta em: %s" % os.getcwd())
    os.system('rm -rf scripts')
    os.system('cp -r C:/scripts_logs/scripts C:/')
    print('\n')
    print('Dados atualizados e copiados...', '\n')
    os.system('git log --oneline')
    #print('\n')
    import sistema
    subprocess.run("sistema.py", shell=True)
    time.sleep(3)

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
#func_pull()

#---------------------------------------------------
