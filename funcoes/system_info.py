import os
import subprocess
from funcoes.interface_test import *


func_cabecalho('Informacoes do Windows')
subprocess.run(["systeminfo"])
dados_pc()