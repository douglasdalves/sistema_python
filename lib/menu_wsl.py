#------------------------------------------------
#Importacao de dados

from variaveis.interface_config import *


#https://docs.microsoft.com/pt-br/windows/wsl/filesystems#:~:text=Execute%20bin%C3%A1rios%20do%20Linux%20no,.exe%20).&text=Bin%C3%A1rios%20invocados%20desta%20maneira%3A,como%20usu%C3%A1rio%20padr%C3%A3o%20do%20WSL.

#------------------------------------------------
#Linhas de personalizacao

myfile_docker = r'C:/sistema_python/automacao_sh/wsl_start_docker.sh'
myfile_stop = r'C:/sistema_python/automacao_sh/wsl_stop_docker.sh'
myfile_pafina = r'C:/sistema_python/sistema.sh'

#------------------------------------------------
# funções

def wsl_status():
    print('\n')
    subprocess.run(["wsl", "-l", "-v"])
    print('\n')


# Dados menu em lista
mlist = [
    'Status do Subsistema wsl2',
    'Stop do Subsistema wsl2',
    'Start docker',
    'Stop docker', 
    'Captura de Tela', 
    'Menu home'
]

#------------------------------------------------
#Codigo do menu 6

def abrir_wsl():
    while True:
        resposta = menu(mlist, 'Menu de Funcoes WSL')
        os.system('cls') or None

        if resposta == 1:
            wsl_status()
        elif resposta == 2:
            print('Stop do Subsistema WS2')
            print('\n','Stop da WSL2','\n')
            os.system('wsl --shutdown && wsl -l -v')
        elif resposta == 3:
            print('Start Docker')
            subprocess.run(myfile_docker, shell=True)
            os.system('wsl docker ps')
            print('\n')
        elif resposta == 4:
            print('Stop Docker')
            os.system('wsl docker ps')
            subprocess.run(myfile_stop, shell=True)
            os.system('wsl docker ps')
        elif resposta == 5:
            gerar_print()
        elif resposta == 6:
            frase_retorno()
        else:
            print("Opção inválida. Tente novamente.")
            time.sleep(2)

if __name__ == "__main__":
    abrir_wsl()