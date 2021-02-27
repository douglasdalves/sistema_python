import os

while True:
    print('\n')
    aplicar = str(input('Voce quer realizar as alteracoes? '))
    if aplicar == 'sim':
        print('\n')
        print('Certo vou aplicar o git add .')
        #os.system('git add .')
        print('Agora precisa commitar, digite abaixo..')
        os.system(input())
        print('\n')
        os.system('git log')
    elif aplicar == 'enviar':
        print('Enviando dados ao Servidor')
        os.system('git push server master')
        print('\n')
    else:
        aplicar == 'nao'
        print('Tudo bem volte quando quiser')
        break