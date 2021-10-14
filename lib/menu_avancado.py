#------------------------------------------------
#Importacao de dados

from variaveis.interface_config import *
from funcoes.info_hardware import *
from time import sleep
import os

#------------------------------------------------
#Linhas de personalizacao

myfile_dns = r'C:/scripts/funcoes/consulta_dns.py'
myfile_netstat = r'C:/scripts/funcoes/netstat_rede.py'

#------------------------------------------------
#Codigo do menu 5

def abrir_avanc():
    while True:
        resposta = menu_secund(['TraceRouter e Pathping','Testar o DNS','Testar com Netstat','Teste1','Captura de Tela','Retornar ao Home'])
        if resposta == 1:
            os.system('cls') or None
            print('Opcao 1 - Testes do Trace na Seanet')
            traceroute()
        elif resposta == 2:
            os.system('cls') or None
            os.startfile(myfile_dns)
        elif resposta == 3:
            print('Opcao 3 - Testando a Rede em Netstat')
            os.system('cls') or None
            os.startfile(myfile_netstat)
        elif resposta == 4:
            print('Opcao 4 - Test')
        elif resposta == 5:
            print('Opcao 5 - Captura de Tela')
            gerar_print()
        elif resposta == 6:
            frase_retorno()
        else:
            leia_opcao()
            sleep(2)