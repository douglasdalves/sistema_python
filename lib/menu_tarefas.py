#------------------------------------------------
#Importacao de dados

from funcoes_tarefas.func_devops import func_devops
from variaveis.interface_config import *
from comp_git.git_test import *

#------------------------------------------------

myfile_programas = Path("C:/sistema_python/funcoes_tarefas/instal_programas.bat")


# Dados menu em lista
mlist = [
    'Pacotes do Python',
    'GitHub',
    'DevOps',
    'Variavel Ambiente',
    'Install Programas', 
    'Captura de Tela', 
    'Voltar'
]

#------------------------------------------------
#Codigo do menu 2

def abrir_taref():
    while True:
        resposta = menu(mlist, 'Menu Tarefas')
        os.system('cls') or None

        if resposta == 1:
            exec(open("./funcoes_tarefas/pacotes_detalhes.py").read())
        elif resposta == 2:
            notas_git()
        elif resposta == 3:
            func_devops()
        elif resposta == 4:
            exec(open("./funcoes_tarefas/func_variavel.py").read())
        elif resposta == 5:
            os.startfile(myfile_programas)
        elif resposta == 6:
            gerar_print()
        elif resposta == 7:
            frase_retorno()
        else:
            print("Opção inválida. Tente novamente.")
            time.sleep(2)

if __name__ == "__main__":
    abrir_taref()