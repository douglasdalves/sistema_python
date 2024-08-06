#------------------------------------------------
#Importacao de dados

from variaveis.interface_config import *
from funcoes.info_hardware import *

#------------------------------------------------

# Dados menu
mlist = [
    'Versao do Windows',
    'Detalhes do Windows',
    'Informacao do Hardware',
    'Rotas do Windows',
    'Processos Windows', 
    'Captura de Tela', 
    'Voltar'
]

myfile_cp_logs = Path("C:/scripts_logs")
myfile_processos = Path("C:/sistema_python/funcoes_tarefas/processos_wind.bat")

#------------------------------------------------

# Função principal que controla o menu
def abrir_autom():
    while True:
        resposta = menu(mlist, 'Menu Automacao')
        os.system('cls') or None

        if resposta == 1:
            versao_windows()
        elif resposta == 2:
            system_info()
        elif resposta == 3:
            info_hardware()
        elif resposta == 4:
            route()
        elif resposta == 5:
            os.startfile(myfile_processos)
        elif resposta == 6:
            gerar_print()
        elif resposta == 7:
            frase_retorno()
        else:
            print("Opção inválida. Tente novamente.")
            time.sleep(2)

if __name__ == "__main__":
    abrir_autom()