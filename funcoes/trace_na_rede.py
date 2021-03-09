import os
import subprocess
from termcolor import colored
from funcoes.interface_test import *


func_cabecalho('Excutando um Traceroute na Seanet')
os.system('tracert 186.251.248.1')

func_cabecalho('Excutando um Pathping na Seanet')
os.system('pathping 186.251.248.1')
dados_pc()
