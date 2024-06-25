#------------------------------------------------
#Importacao de dados

from variaveis.interface_config import *
from funcoes.info_hardware import *

#------------------------------------------------
#Linhas de personalizacao

myfile_dns = Path("C:/sistema_python/funcoes/consulta_dns.py")
myfile_netstat = Path("C:/sistema_python/funcoes/netstat_rede.py")

# Dados menu
t_menu = 'TraceRouter e Pathping'
t_menu1 = 'Testar o DNS'
t_menu2 = 'Testar com Netstat'

#------------------------------------------------
#Codigo do menu 3

def abrir_avanc():
    while True:
        resposta = menu_secund([t_menu,t_menu1,t_menu2,opcao_captura,opcao_retorno])
        if resposta == 1:
            os.system('cls') or None
            print('{}'.format(op1), 'Testes do Trace na Seanet')
            traceroute()
        elif resposta == 2:
            os.system('cls') or None
            os.startfile(myfile_dns)
        elif resposta == 3:
            print('{}'.format(op3), 'Testando a Rede em Netstat')
            os.system('cls') or None
            os.startfile(myfile_netstat)
        elif resposta == 4:
            print('{}'.format(op4), 'Captura de Tela')
            gerar_print()
        elif resposta == 5:
            frase_retorno()
        else:
            leia_opcao()
            sleep(2)