#------------------------------------------------
#Importacao de dados

from variaveis.interface_config import *
from funcoes.info_hardware import *

#------------------------------------------------
#Linhas de personalizacao

myfile_dns = Path("C:/sistema_python/funcoes/consulta_dns.py")
myfile_netstat = Path("C:/sistema_python/funcoes/netstat_rede.py")


# Dados menu em lista
mlist = [
    'TraceRouter e Pathping',
    'Testar o DNS',
    'Testar com Netstat', 
    'Captura de Tela', 
    'Voltar'
]

#------------------------------------------------

# Função principal que controla o menu
def abrir_avanc():
    while True:
        resposta = menu(mlist, 'Menu Avancado de Rede')
        os.system('cls') or None

        if resposta == 1:
            traceroute()
        elif resposta == 2:
            os.startfile(myfile_dns)
        elif resposta == 3:
            os.startfile(myfile_netstat)
        elif resposta == 4:
            gerar_print()
        elif resposta == 5:
            frase_retorno()
        else:
            print("Opção inválida. Tente novamente.")
            time.sleep(2)

if __name__ == "__main__":
    abrir_avanc()