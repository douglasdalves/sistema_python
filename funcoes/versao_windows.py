import subprocess
from funcoes.interface_test import *

func_cabecalho('Detalhes da versao do SO')

print('\n')
subprocess.run(["wmic", "os", "get", "buildnumber,caption,CSDVersion"])
subprocess.run(["wmic", "OS", "get", "OSArchitecture"])
dados_pc()

subprocess.run(["winver"])