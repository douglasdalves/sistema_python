#------------------------------------------------
#Importacao de dados

from email.mime import application
from lib.menu_tarefas import abrir_taref
from lib.menu_avancado import abrir_avanc
from lib.menu_automacao import abrir_autom
from lib.menu_wsl import abrir_wsl
from variaveis.interface_config import *

from funcoes import *
from lib import *
import curses

#------------------------------------------------

# Dados menu em lista
mlist = [
    'Teste de Conexao ao Provedor', 
    'Agilizando Tarefas', 
    'Teste de Rede', 
    'Testes Automatizados', 
    'Tarefas em WSL',
    'Web system', 
    'Captura de Tela', 
    'Sair'
]

submenu1 = ['TraceRouter e Pathping', 'Testar o DNS', 'Testar com Netstat', 'Captura de Tela',  'Voltar']
submenu2 = ['Opção 2.1', 'Opção 2.2', 'Voltar']
submenu3 = ['Opção 3.1', 'Opção 3.2', 'Voltar']
submenu4 = ['Opção 4.1', 'Opção 4.2', 'Voltar']


def menu(stdscr, menu_list, title):
    curses.curs_set(0)
    current_row = 0

    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()
        # margin_top = 3
        # menu_start_y = margin_top
        menu_start_y = 5
        stdscr.addstr(menu_start_y - 2, 6, title)

        for idx, row in enumerate(menu_list):
            x = 2  # Posição fixa à esquerda
            y = menu_start_y + idx
            if idx == current_row:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, row)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y, x, row)

        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu_list) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            return current_row + 1

        stdscr.refresh()



# Função principal que controla o menu
def tela_principal(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    while True:
        resposta = menu(stdscr, mlist, 'MENU PRINCIPAL')
        os.system('cls') or None
        
        if resposta == 1:
            exec(open("./funcoes/conexao_seanet.py").read())
        elif resposta == 2:
            submenu(stdscr, submenu1, 'Menu Automacao')
            abrir_taref()
        elif resposta == 3:
            submenu(stdscr, submenu2, 'Menu Avancado de Rede')
            #abrir_avanc()
        elif resposta == 4:
            submenu(stdscr, submenu3, 'Menu Tarefas')
            #abrir_autom()
        elif resposta == 5:
            submenu(stdscr, submenu4, 'Menu de Funcoes WSL')
            #abrir_wsl()
        elif resposta == 6:
            os.startfile('aplication.html')
        elif resposta == 7:
            gerar_print()
        elif resposta == 8:
            funcao_sair()
            break
        else:
            print("Opção inválida. Tente novamente.")
            time.sleep(2)


def submenu(stdscr, submenu_list, title):
    while True:
        resposta = menu(stdscr, submenu_list, title)
        os.system('cls') or None
        
        if resposta == len(submenu_list):
            break
        else:
            print(f'Selecionado: {submenu_list[resposta - 1]}')
            time.sleep(1)

if __name__ == "__main__":
    curses.wrapper(tela_principal)


from funcoes.info_hardware import *

#------------------------------------------------
#Linhas de personalizacao

myfile_dns = Path("C:/sistema_python/funcoes/consulta_dns.py")
myfile_netstat = Path("C:/sistema_python/funcoes/netstat_rede.py")


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