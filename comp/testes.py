import subprocess
import os
import platform




print(platform.system())
print(platform.version())
print(platform.node())
print(platform.processor())
print('\n')

import getpass
print(getpass.getuser())
print(getpass.())




def dados_pc():
    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
    cpu = platform.node()
    user = getpass.getuser()
    print('\n')
    print('--------- Testes Concluidos ---------')
    print(colored(f'Data e Hora do teste: {data_e_hora_em_texto}', 'blue', attrs=['bold']))
    print(colored(f'Equipamento do Teste: {cpu}', 'blue', attrs=['bold']))
    print(colored(f'Usuario do Sistema: {user}', 'blue', attrs=['bold']))
    print('\n')