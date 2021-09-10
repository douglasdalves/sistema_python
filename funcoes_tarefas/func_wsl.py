
from termcolor import colored
from variaveis.interface_config import *


def wsl_status():
    func_cabecalho('Dados dos Subsistemas')
    print('\n')
    subprocess.run(["wsl", "-l", "-v"])
    print('\n')