import subprocess
from funcoes.interface_test import *


def versao_windows():
    func_cabecalho('Detalhes da versao do SO')
    print('\n')
    subprocess.run(["wmic", "os", "get", "buildnumber,caption,CSDVersion"])
    subprocess.run(["wmic", "OS", "get", "OSArchitecture"])
    dados_pc()
    subprocess.run(["winver"])

def system_info():
    func_cabecalho('Informacoes do Windows')
    subprocess.run(["systeminfo"])
    dados_pc()