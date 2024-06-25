
#------------------------------------------------

from variaveis.interface_config import *

#------------------------------------------------


def linha_devops(tam = 42):
    return '-' * tam

def cabecalho_devops (txt):
    print('\n')
    print(linha_devops())
    print(txt.center(42))
    print(linha_devops())
    print('\n')

#------------------------------------------------
# funcoes do cenario git

f1 = ('Permite ver todas as maquinas que estao rodando.')
f2 = ('Permite ver quais os boxes que estao instalados.')
f3 = ('Permite ver os containers.')
f4 = ('Permite ver as images em docker.')
f5 = ('Permite ver as Wsl na maquina')

f6 = ('Dados do AWS configure')
f7 = ('Dados da versão do CLI')
f8 = ('Dados do configure - profile')
f9 = ('Dados do config do aws cli')
f10 = ('setx AWS_PROFILE nomeProf')

#------------------------------------------------

def func_devops():
    aplicar = 0
    while aplicar != 6:
        print('''Opcoes:
        [1] Voltar ao menu
        [2] Todas as opcoes
        [3] Dados WSL
        [4] Dados Docker
        [5] Dados AWS cli
        [6] Dados Vagrant
        [7] Abrir o vsCode''')
        print('\n')
        aplicar = str(input('Digite uma opcao? '))
        if aplicar == '1':
            cabecalho_devops('Tudo bem volte quando quiser')
            break
        elif aplicar == '2':
            dev_wsl()
            dev_docker()
            #dev_vagrant()
        elif aplicar == '3':
            dev_wsl()
        elif aplicar == '4':
            dev_docker()
        elif aplicar == '5':
            aws_cli()
        elif aplicar == '6':
            print('funcao desativada')
        else:
            aplicar == '7'
            os.system('code .')

#------------------------------------------------

def dev_wsl():
    cabecalho_devops('Funcoes em WSL')

    print(colored('{}'.format(f5), 'blue', attrs=['bold']), '\n')
    #os.system('wsl -l -v')
    os.system('wsl ~ -e sh -c "ls -l"')
    print('\n')

#------------------------------------------------

def dev_docker():
    cabecalho_devops('Funcoes em Docker')

    print(colored('{}'.format(f3), 'blue', attrs=['bold']), '\n')
    os.system('docker ps -a')
    print('\n')
    print(colored('{}'.format(f4), 'blue', attrs=['bold']), '\n')
    os.system('docker images')
    print('\n')

#------------------------------------------------

def aws_cli():
    cabecalho_devops('Funcoes do AWS cli')

    print(colored('{}'.format(f6), 'blue', attrs=['bold']), '\n')
    os.system('cat ~/.aws/credentials')
    print('\n')
    print(colored('{}'.format(f9), 'blue', attrs=['bold']), '\n')
    os.system('cat ~/.aws/config')
    print('\n')
    print(colored('{}'.format(f7), 'blue', attrs=['bold']), '\n')
    os.system('aws configure --version')
    print('\n')
    print(colored('{}'.format(f8), 'blue', attrs=['bold']), '\n')
    os.system('aws configure list')
    print('\n')
    print(colored('{}'.format(f10), 'blue', attrs=['bold']), '\n')
    os.system('aws configure list-profiles')
    print('\n')


# def dev_vagrant():
#     cabecalho_devops('Funcoes em Vagrant')

#     print(colored('{}'.format(f1), 'blue', attrs=['bold']), '\n')
#     os.system('vagrant global-status')
#     print('\n')
#     print(colored('{}'.format(f2), 'blue', attrs=['bold']), '\n')
#     os.system('vagrant box list')